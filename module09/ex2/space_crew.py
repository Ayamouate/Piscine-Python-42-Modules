from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Contact ID must start with \"M\"")
        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")
        if self.duration_days > 365:
            exp_cont = sum(member.years_experience >= 5
                           for member in self.crew)
            if exp_cont / len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50%"
                                 " experienced crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def display_space_mission(mission: SpaceMission) -> None:
    print("========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f" - {member.name} ({member.rank.value}) "
              f"- {member.specialization}")
    print("\n========================================")


def main() -> None:
    print("Space Mission Crew Validation")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(member_id="C001",
                           name="Sarah Connor",
                           rank=Rank.COMMANDER,
                           age=40,
                           specialization="Mission Command",
                           years_experience=12),
                CrewMember(member_id="C002",
                           name="John Smith",
                           rank=Rank.LIEUTENANT,
                           age=35,
                           specialization="Navigation",
                           years_experience=6),
                CrewMember(member_id="C003",
                           name="Alice Johnson",
                           rank=Rank.OFFICER,
                           age=30,
                           specialization="Engineering",
                           years_experience=8)
            ],
            budget_millions=2500.0
        )
        display_space_mission(valid_mission)
    except ValidationError as e:
        for err in e.errors():
            print("Expected validation error:")
            error_msg = err["msg"].split(",", 1)[1].strip()
            print(error_msg)
    try:
        invalide_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(member_id="C004",
                           name="Mark Lee",
                           rank=Rank.LIEUTENANT,
                           age=34,
                           specialization="Navigation",
                           years_experience=3),
                CrewMember(member_id="C005",
                           name="Anna Bell",
                           rank=Rank.OFFICER,
                           age=28,
                           specialization="Science",
                           years_experience=2)
            ],
            budget_millions=1000.0
        )
        display_space_mission(invalide_mission)
    except ValidationError as e:
        for err in e.errors():
            print("Expected validation error:")
            error_msg = err["msg"].split(",", 1)[1].strip()
            print(error_msg)


if __name__ == "__main__":
    main()
