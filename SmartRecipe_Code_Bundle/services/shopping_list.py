"""
Shopping List — What the User Still Needs to Buy
================================================
Compares what the user has vs what the recipe needs.
Missing items are split into:
1. Pantry items (oil, salt, pepper, soy sauce) — many people already have these
2. Things to buy — main ingredients they probably need to get
"""

# Items we treat as "pantry staples" — shown separately as "you may already have"
PANTRY_STAPLES = {"oil", "salt", "pepper", "soy sauce"}

# Returns list of ingredients the recipe needs that the user doesn't have
def generate_shopping_list(available_ingredients, recipe_ingredients):
    available = set([i.strip().lower() for i in available_ingredients])
    return [item for item in recipe_ingredients if item.lower() not in available]

# Same as above, but splits into "pantry" vs "to buy"
# Pantry = oil, salt, etc. | To buy = chicken, potato, etc.
def generate_shopping_list_split(available_ingredients, recipe_ingredients):
    missing = generate_shopping_list(available_ingredients, recipe_ingredients)
    pantry = [m for m in missing if m.lower() in PANTRY_STAPLES]
    to_buy = [m for m in missing if m.lower() not in PANTRY_STAPLES]
    return {"pantry": pantry, "to_buy": to_buy}
