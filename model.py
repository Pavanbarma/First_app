from pydantic import BaseModel
from typing import Dict, List


class Positions(BaseModel):
    positions: Dict[str, str]
