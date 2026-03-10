"""
Diet-ingredient compatibility check.
Warns users when they select a diet but enter ingredients that typically conflict with that diet.
"""

# Ingredients that typically conflict with each diet (lowercase, for matching)
# Uses partial matching: "egg" matches "eggs", "egg white"; "chicken" matches "chicken breast"
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
        # Root vegetables (avoided because uprooting kills the plant)
        "onion", "garlic", "potato", "carrot", "beetroot", "radish",
        "ginger", "turmeric", "sweet potato", "yam", "turnip",
    },
    "High Protein": set(),  # No exclusions; it's a preference
}


def get_conflicting_ingredients(ingredients, diet):
    """
    Returns list of ingredients that typically conflict with the selected diet.
    Returns empty list if diet is None, diet has no conflicts, or no conflicts found.
    """
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


def get_diet_guidance(diet):
    """Returns a short guidance string for what the diet typically excludes."""
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
