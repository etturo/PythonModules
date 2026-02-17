#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    if ("fire" in ingredients.lower() or
            "air" in ingredients.lower() or
            "water" in ingredients.lower() or
            "hearth" in ingredients.lower()):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
