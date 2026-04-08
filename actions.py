from dataclasses import dataclass


@dataclass
class EditAction:
    new_code: str


@dataclass
class RunTestsAction:
    pass