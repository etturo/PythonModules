#!/usr/bin/env python3
def mage_counter() -> callable:
    count: int = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> callable:
    power: int = initial_power

    def increment():
        nonlocal power
        power += 1
        return power

    return increment


def enchantment_factory(enchantment_type: str) -> callable:

    def apply_enchantment(item_name):
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key, value):
        vault[key] = value
        return f"Memory stored: {key}"

    def recall(key):
        return vault.get(key, "Memory not fuond")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(10)
    print(f"Call 1: {accumulator()}")
    print(f"Call 2: {accumulator()}")
    print(f"Call 3: {accumulator()}")

    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print()

    print("Testing memory vault...")
    vault = memory_vault()
    print(vault['store']("hero", "Arthas"))
    print(vault['store']("spell", "Fireball"))
    print(vault['recall']("hero"))
    print(vault['recall']("spell"))
    print(vault['recall']("unknown"))

    print()


if __name__ == "__main__":
    main()
