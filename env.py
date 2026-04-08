from openenv.env import Env

from actions import EditAction, RunTestsAction
from schemas import CodeObservation, StepResult
from utils.executor import run_code

import tasks.easy_bugfix as easy
import tasks.medium_refactor as medium
import tasks.hard_feature as hard

import graders.easy_grader as easy_grader
import graders.medium_grader as medium_grader
import graders.hard_grader as hard_grader

TASKS = {
    "easy": easy,
    "medium": medium,
    "hard": hard
}

GRADERS = {
    "easy": easy_grader,
    "medium": medium_grader,
    "hard": hard_grader
}


class CodeAssistEnv(Env):

    def __init__(self, task_name="easy"):
        super().__init__()
        self.task_name = task_name
        self.task = TASKS[task_name]

    def reset(self) -> CodeObservation:
        self.state = self.task.init()
        self.state["last_output"] = ""
        self.state["steps"] = 0

        return CodeObservation(**self.state)

    def step(self, action) -> StepResult:

        reward = 0.0
        done = False

        self.state["steps"] += 1

        # 🔥 IMPORTANT: typed action handling
        if isinstance(action, EditAction):
            self.state["code"] = action.new_code
            reward -= 0.05

        elif isinstance(action, RunTestsAction):

            grader = GRADERS[self.task_name]
            score = grader.grade(self.state)

            reward += score
            self.state["last_output"] = f"Score: {score}"

            if score == 1.0:
                reward += 1.0
                done = True

        if self.state["steps"] > 15:
            reward -= 0.1

        obs = CodeObservation(**self.state)

        return StepResult(
            observation=obs,
            reward=reward,
            done=done,
            info={}
        )

    def state(self):
        return self.state