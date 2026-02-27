#!/usr/bin/env python3
from enum import Enum, auto
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = auto()
    visual = auto()
    physical = auto()
    telepathic = auto()


class AlienContact(BaseModel):
    contact_id: str = Field(max_length=15, min_length=5)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(strict=True)
    signal_strength: float = Field(gt=0.0, lt=10.0)
    duration_minutes: int = Field(gt=1, lt=1440)
    witness_count: int = Field(gt=1, lt=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=True)

    @model_validator(mode='after')
    def validate(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must begin with 'AC'")
        if self.is_verified is False and \
                self.contact_type == ContactType.physical:
            raise ValueError("Physical contact MUST be verified")
        if self.contact_type == ContactType.telepathic and \
                self.witness_count < 3:
            raise ValueError("Thelepatic contact "
                             "requires at least 3 witnesses")
        if self.signal_strength > 7.0 and \
                self.message_received is None:
            raise ValueError("Strong signal should include "
                             "received message")
        return self


def main():
    print()

    print("Alien Contact Log Validation")

    print("=" * 42)

    try:
        ac = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}/10")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: {ac.message_received}")

        print()
    except ValidationError as e:
        for error in e.errors():
            if len(error['loc']) > 0:
                err_name: str = error['loc'][0]
            else:
                err_name: str = "Model Logic"
            err_msg: str = error['msg']
            print(f"[ERROR] {err_name}: {err_msg}")

    print("=" * 42)

    print("Expected validation Error:")
    try:
        ac = AlienContact(
            contact_id="AC_2024_002",
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=5.3,
            duration_minutes=45,
            witness_count=2,
            message_received=""
        )
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}/10")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: {ac.message_received}")

        print()
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
