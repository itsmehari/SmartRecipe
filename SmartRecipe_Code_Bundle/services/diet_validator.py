"""
Diet Validator — Checks If Ingredients Match the Chosen Diet
============================================================
If user picked "Vegan" but typed "egg" or "chicken", we warn them.
We don't block — just show a friendly warning so they can fix it.

Also provides ingredient-based diet inference for recipes — so we classify
veg/non-veg/vegan/jain from actual ingredients, not just CSV tags.
"""

# ----- INGREDIENT-BASED DIET INFERENCE -----
# Used to validate/override recipe diet tags from CSV
NON_VEG_INGREDIENTS = {
    "chicken", "beef", "pork", "lamb", "mutton", "fish", "shrimp", "prawn",
    "meat", "seafood", "crab", "lobster", "bacon", "ham", "sausage", "egg",
}
DAIRY_EGG_INGREDIENTS = {
    "egg", "milk", "butter", "cheese", "cream", "yogurt", "honey",
    "ghee", "gelatin", "whey", "casein",
}
JAIN_AVOID_INGREDIENTS = {
    "onion", "garlic", "potato", "carrot", "beetroot", "radish",
    "ginger", "turmeric", "sweet potato", "yam", "turnip",
}


def infer_recipe_diet(ingredients):
    """
    Infer correct diet tags from recipe ingredients.
    Overrides CSV tags — a recipe with chicken is Non-Vegetarian, never Vegetarian.
    Returns list of valid diet strings.
    """
    if not ingredients:
        return []
    ings = {i.strip().lower() for i in ingredients if i and isinstance(i, str)}
    # Also check substrings: "chicken breast" contains "chicken"
    def has_any(ing_set):
        for ing in ings:
            for term in ing_set:
                if term in ing or ing in term:
                    return True
        return False

    diets = []
    if has_any(NON_VEG_INGREDIENTS):
        diets = ["Non-Vegetarian", "High Protein"]
    else:
        diets = ["Vegetarian", "High Protein"]
        if not has_any(DAIRY_EGG_INGREDIENTS):
            diets.insert(1, "Vegan")
        if not has_any(JAIN_AVOID_INGREDIENTS):
            diets.append("Jain")
    return diets


# For each diet, list of ingredients that typically don't belong
# Example: Vegetarian = no meat, fish, seafood
DIET_CONFLICTS = {
    "Vegetarian": {
        "meat", "chicken", "beef", "pork", "lamb", "mutton", "fish", "seafood",
        "shrimp", "prawn", "crab", "lobster", "bacon", "ham", "sausage",
    },
    "Vegan": {
        "meat", "chicken", "beef", "pork", "lamb", "mutton", "fish", "seafood",
        "shrimp", "prawn", "crab", "lobster", "bacon", "ham", "sausage",
        "egg", "milk", "butter", "cheese", "cream", "yogurt", "honey",
        "gelatin", "ghee", "whey", "casein",
    },
    "Jain": {
        # Animal products
        "meat", "chicken", "beef", "pork", "lamb", "mutton", "fish", "seafood",
        "shrimp", "prawn", "crab", "lobster", "bacon", "ham", "sausage",
        "egg", "milk", "butter", "cheese", "cream", "yogurt", "honey",
        # Root vegetables (Jain diet avoids these)
        "onion", "garlic", "potato", "carrot", "beetroot", "radish",
        "ginger", "turmeric", "sweet potato", "yam", "turnip",
    },
    "High Protein": set(),  # No exclusions — it's a preference, not a restriction
}

# Returns list of user ingredients that conflict with the chosen diet
# Example: get_conflicting_ingredients(["tomato", "egg"], "Vegan") -> ["egg"]
def get_conflicting_ingredients(ingredients, diet):
    if not diet or diet == "None":
        return []
    if diet not in DIET_CONFLICTS:
        return []
    conflicts_set = DIET_CONFLICTS[diet]
    if not conflicts_set:
        return []

    conflicting = []
    for ing in ingredients:
        ing_lower = ing.strip().lower()
        if not ing_lower:
            continue
        for conflict_term in conflicts_set:
            if conflict_term in ing_lower or ing_lower in conflict_term:
                conflicting.append(ing)
                break
    return conflicting

# Returns a short sentence explaining what each diet excludes
# Used in the warning message (e.g. "Vegan excludes meat, fish, eggs...")
def get_diet_guidance(diet):
    if not diet or diet == "None":
        return ""
    guidance = {
        "Vegetarian": "excludes meat, fish, seafood",
        "Vegan": "excludes all animal products (meat, fish, eggs, dairy, honey)",
        "Non-Vegetarian": "includes chicken, fish, egg, prawn (excludes pure veg recipes)",
        "Jain": "excludes meat, fish, eggs, and root vegetables (onion, garlic, potato, carrot)",
        "High Protein": "no exclusions",
    }
    return guidance.get(diet, "")
