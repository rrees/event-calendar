from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Event:
    id: int
    external_id: str
    start_date: str
    end_date: str
    name: str
    url: Optional[str]
    comment: Optional[str]
    created: datetime
    updated: datetime
