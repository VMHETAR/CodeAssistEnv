from dataclasses import dataclass
from typing import List, Any, Dict

@dataclass
class StepResult:
    observation: Any
    reward: float
    done: bool
    info: Dict
from typing import List

@dataclass
class CodeObservation:
    code: str
    tests: List[str]
    last_output: str
    steps: int
