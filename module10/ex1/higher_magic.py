#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args: multiplier * base_spell(*args)


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args: [spell(*args) for spell in spells]


def add(x):
    return x + 10


def double(x):
    return x * 2


def fire_bolt(x):
    return x + 3


def is_even(x):
    return x % 2 == 0


def magic(x):
    return f"Magic on {x}!"


def square(x):
    return x ** 2


def minus_one(x):
    return x - 1


def spell_str(x):
    return f"spell({x})"


def main():
    print()

    print("spell_combiner:")
    combined = spell_combiner(double, add)
    print(f"double(5) = {double(5)}")
    print(f"add(5) = {add(5)}")
    print(f"combined(5) = {combined(5)}")

    print()

    print("power_amplifier")
    amplified = power_amplifier(fire_bolt, 4)
    print(f"fire_bolt(7) = {fire_bolt(7)}")
    print(f"amplified(7) = {amplified(7)}")

    print()

    print("conditional_caster")
    caster = conditional_caster(is_even, magic)
    print(f"caster(4) = {caster(4)}")
    print(f"caster(7) = {caster(7)}")

    print()

    print("spell_sequence")
    sequence = spell_sequence([square, minus_one, spell_str])
    print(f"sequence(6) = {sequence(6)}")

    print()


if __name__ == "__main__":
    main()
