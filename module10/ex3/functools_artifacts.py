#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operation_map: dict[str, callable] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }

    selected_function = operation_map.get(operation)
    return reduce(selected_function, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, "Fire"),
        'ice_enchant': partial(base_enchantment, 50, "Ice"),
        'lightning_enchant': partial(base_enchantment, 50, "Lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(target) -> str:
        return f"A mysterious magical aura surrounds {target}..."

    @cast_spell.register(int)
    def _(power) -> str:
        return f"Blasted the enemy for {power} magical damage!"

    @cast_spell.register(str)
    def _(item) -> str:
        return f"Enchanted the {item} with glowing runes!"

    @cast_spell.register(dict)
    def _(targets) -> str:
        return f"Multi-casting on {len(targets)} targets: {', '.join(targets)}"

    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [20, 30, 40, 10]

    print()

    sum_result = spell_reducer(spells, 'add')
    product_result = spell_reducer(spells, 'multiply')
    max_result = spell_reducer(spells, 'max')

    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")
    print(f"Max: {max_result}")

    print()

    print("Testing memoized fibonacci...")
    fib_10 = memoized_fibonacci(10)
    fib_15 = memoized_fibonacci(15)

    print(f"Fib(10): {fib_10}")
    print(f"Fib(15): {fib_15}")

    print()

    print("Testing partial enchanter...")

    def base_enchantment(power: int, element: str, item: str) -> str:
        return f"Enchanted {item} with {power} units of {element} magic"

    enchantments = partial_enchanter(base_enchantment)
    print(enchantments['fire_enchant']('sword'))
    print(enchantments['ice_enchant']('shield'))
    print(enchantments['lightning_enchant']('staff'))

    print()

    print("Testing spell dispatcher...")
    cast_spell = spell_dispatcher()

    print(cast_spell("mysterious artifact"))
    print(cast_spell(75))
    print(cast_spell("bow"))
    print(cast_spell({'goblin': 1, 'orc': 2, 'dragon': 1}))

    print()
