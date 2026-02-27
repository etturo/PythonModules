#!/urs/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=1, lt=20)
    power_level: float = Field(gt=0.0, lt=100.0)
    oxygen_level: float = Field(gt=0.0, lt=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("\nSpace Station Data Validation")
    print("=" * 42)

    try:
        iss = SpaceStation(
            station_id="ISS001",
            name="Internation Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True
        )

        print("Valid station created:")
        print(f"ID: {iss.station_id}")
        print(f"Name: {iss.name}")
        print(f"Crew: {iss.crew_size} people")
        print(f"Power: {iss.power_level}%")
        print(f"Oxygen: {iss.oxygen_level}%")
        if iss.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: off")

    except ValidationError as e:
        for error in e.errors():
            if len(error['loc']) > 0:
                err_name: str = error['loc'][0]
            else:
                err_name: str = "Model Logic"
            err_msg: str = error['msg']
            print(f"[ERROR] {err_name}: {err_msg}")

    print()

    print("=" * 42)
    print("Expected validation error:")
    try:
        iss = SpaceStation(
            station_id="jsofoijfsoifjsofjsoifsjoifjs",
            name="Internation Space Stationsldfksd[pfks[fks[fk]]]",
            crew_size=45345,
            power_level=4535353,
            oxygen_level=9534535,
            is_operational=True
        )

        print("Valid station created:")
        print(f"ID: {iss.station_id}")
        print(f"Name: {iss.name}")
        print(f"Crew: {iss.crew_size} people")
        print(f"Power: {iss.power_level}%")
        print(f"Oxygen: {iss.oxygen_level}%")
        if iss.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: off")

    except ValidationError as e:
        for error in e.errors():
            if len(error['loc']) > 0:
                err_name: str = error['loc'][0]
            else:
                err_name: str = "Model Logic"
            err_msg: str = error['msg']
            print(f"[ERROR] {err_name}: {err_msg}")


if __name__ == "__main__":
    main()
