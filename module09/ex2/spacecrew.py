#!/usr/bin/env python3
from enum import Enum, auto
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    cadet = auto()
    officer = auto()
    lieuteant = auto()
    captain = auto()
    commander = auto()


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=3, max_length=50)
    rank: Rank = Field(strict=True)
    age: int = Field(gt=18, lt=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(gt=0, lt=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(gt=1, lt=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(gt=1.0, lt=10000.0)

    @model_validator(mode='after')
    def validator(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(crewmate.rank in (Rank.captain, Rank.commander)
                   for crewmate in self.crew):
            raise ValueError("The Crew must have at least one "
                             "Commander or Captain")
        if self.duration_days > 365 and \
                sum(crewmate.years_experience >= 5
                    for crewmate in self.crew) < len(self.crew)/2:
            raise ValueError("Long mission requires experienced crews")
        if any(not crewmate.is_active for crewmate in self.crew):
            raise ValueError("All crewmates should be active")
        return self


def main():
    print()
    print("Space Mission Crew Validation")
    print("=" * 42)

    sarah: CrewMember = CrewMember(
        member_id="4928",
        name="Sarah Connor",
        rank=Rank.captain,
        age=42,
        specialization="Command",
        years_experience=2,
        is_active=True
    )

    john: CrewMember = CrewMember(
        member_id="4929",
        name="John Smith",
        rank=Rank.officer,
        age=35,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )

    alice: CrewMember = CrewMember(
        member_id="4930",
        name="Alice Johnson",
        rank=Rank.lieuteant,
        age=29,
        specialization="Engineering",
        years_experience=20,
        is_active=True
    )

    pier: CrewMember = CrewMember(
        member_id="4931",
        name="Pier Ports",
        rank=Rank.lieuteant,
        age=29,
        specialization="Engineering",
        years_experience=20,
        is_active=True
    )

    try:
        sm = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status="planned",
            budget_millions=500.0
        )
        print(f"Mission: {sm.mission_name}")
        print(f"ID: {sm.mission_id}")
        print(f"Destination: {sm.destination}")
        print(f"Budget: ${sm.budget_millions} million")
        print(f"Duration: {sm.duration_days} days")
        print(f"Crew Size: {len(sm.crew)}")
        print(f"Crew Members: {', '.join(crew.name for crew in sm.crew)}")
        print()

        print("=" * 42)
        print("Expected validation error after crew change:")

        sm2 = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            crew=[pier, john, alice],
            mission_status="planned",
            budget_millions=500.0
        )
        print(f"Mission: {sm2.mission_name}")
        print(f"ID: {sm2.mission_id}")
        print(f"Destination: {sm2.destination}")
        print(f"Budget: ${sm2.budget_millions} million")
        print(f"Duration: {sm2.duration_days} days")
        print(f"Crew Size: {len(sm2.crew)}")
        print(f"Crew Members: {', '.join(crew.name for crew in sm2.crew)}")

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
