#!/usr/bin/env python3
from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    print(f"Casting {func.__name__}")

    @wraps(func)
    def timer(*args):
        start: float = time.time()

        result = func(*args)

        end: float = time.time()

        print(f"Spell completed in {end - start} seconds")
        return result

    return timer


def power_validator(min_power: int) -> callable:

    def decorator(func):

        @wraps(func)
        def wrapper(*args):
            if args[2] >= min_power:
                return func(*args)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(
                            char.isalpha() or char.isspace() for char in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    print()

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Ab"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
