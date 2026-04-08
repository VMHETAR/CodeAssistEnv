from env import CodeAssistEnv
from actions import EditAction, RunTestsAction

def run():

    env = CodeAssistEnv("easy")
    obs = env.reset()

    for _ in range(10):

        # dummy agent logic
        if obs.last_output == "":
            action = RunTestsAction()
        else:
            action = EditAction(new_code=obs.code.replace("-", "+"))

        result = env.step(action)
        obs = result.observation

        if result.done:
            break


if __name__ == "__main__":
    run()