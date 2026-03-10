PANTRY_STAPLES = {"oil", "salt", "pepper", "soy sauce"}

def generate_shopping_list(available_ingredients, recipe_ingredients):
    """Returns list of missing ingredients."""
    available = set([i.strip().lower() for i in available_ingredients])
    return [item for item in recipe_ingredients if item.lower() not in available]

def generate_shopping_list_split(available_ingredients, recipe_ingredients):
    """Returns {'pantry': [...], 'to_buy': [...]} — pantry items many users have."""
    missing = generate_shopping_list(available_ingredients, recipe_ingredients)
    pantry = [m for m in missing if m.lower() in PANTRY_STAPLES]
    to_buy = [m for m in missing if m.lower() not in PANTRY_STAPLES]
    return {"pantry": pantry, "to_buy": to_buy}
