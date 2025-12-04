from dataclasses import dataclass
from datetime import datetime

@dataclass
class Advertisement:
    id: int | None
    title: str
    description: str
    created_at: str
    owner: str
