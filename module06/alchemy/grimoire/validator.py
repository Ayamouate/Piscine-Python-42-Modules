

def validate_ingredients(ingredients: str) -> str:
    ingrd = ingredients.split()
    valid = ["fire", "air", "water", "earth"]
    for i in ingrd:
        if i not in valid:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
