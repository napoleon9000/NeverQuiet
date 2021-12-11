import abc
from dataclasses import dataclass
from typing import List


@dataclass
class Status:
    location: List[float]
