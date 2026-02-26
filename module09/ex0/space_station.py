#!/urs/bin/env python3
from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str]

    @model_validator(mode='after')
    def validate(self):
        


def main():
    print("\nSpace Station Data Validation")
    print("=" * 42)

    SpaceStation



if __name__ == "__main__":
    main()