#!/usr/bin/env python3
from functools import reduce, partial
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


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass
