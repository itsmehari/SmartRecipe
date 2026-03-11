"""
Recipe Engine — Finds Which Recipes Match the User's Ingredients
================================================================
Loads recipes from a CSV file, compares them to what the user has, and splits results into:
1. "You can make" — user has at least half the ingredients
2. "Close" — user has 2+ ingredients but less than half

Uses ingredient-based diet inference — recipes are classified by their actual
ingredients (chicken → Non-Veg), not just CSV tags, for robustness.
Cuisine matching is case-insensitive and handles variations.
"""

import csv
from pathlib import Path

from .diet_validator import infer_recipe_diet

# ----- NORMALIZE CUISINE -----
# Handles case and common variations (Italian, italian, etc.)
def _normalize_cuisine(cuisine):
    if not cuisine:
        return ""
    c = cuisine.strip()
    if not c:
        return ""
    # Title case for consistency; handle "South Indian" -> "Indian" for filtering
    lower = c.lower()
    if "indian" in lower or "north indian" in lower or "south indian" in lower:
        return "Indian"
    if "asian" in lower:
        return "Asian"
    if "italian" in lower:
        return "Italian"
    return c.title()


# ----- LOAD RECIPES FROM CSV FILE -----
# Reads recipes.csv: each row has name, cuisine, ingredients, steps, diet, etc.
# Diet is inferred from ingredients (not trusted from CSV alone) for robustness.
def _load_recipes_from_csv():
    base = Path(__file__).resolve().parent.parent
    for data_dir in [base / "data", base.parent / "SmartRecipe_Code_Bundle" / "data", Path.cwd() / "data"]:
        csv_path = data_dir / "recipes.csv"
        if csv_path.exists():
            break
    else:
        return None
    recipes = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Split ingredients string into a list
            ingredients = [i.strip().lower() for i in row.get("ingredients", "").split(",") if i.strip()]
            steps_str = row.get("steps", "")
            steps = [s.strip() for s in steps_str.split("|") if s.strip()] if steps_str else []
            # Infer diet from ingredients — overrides CSV for correct veg/non-veg classification
            diet = infer_recipe_diet(ingredients)
            cuisine_raw = row.get("cuisine", "").strip()
            recipes.append({
                "name": row.get("recipe_name", "").strip(),
                "ingredients": ingredients,
                "cuisine": cuisine_raw,
                "cuisine_normalized": _normalize_cuisine(cuisine_raw),
                "difficulty": row.get("difficulty", "").strip(),
                "diet": diet,
                "steps": steps if steps else ["See recipe instructions."],
            })
    return recipes if recipes else None

# ----- FALLBACK: IF NO CSV, USE THESE 3 RECIPES -----
def _make_fallback_recipe(name, ingredients, cuisine, difficulty, steps):
    """Build fallback recipe with inferred diet and normalized cuisine."""
    diet = infer_recipe_diet(ingredients)
    return {
        "name": name,
        "ingredients": ingredients,
        "cuisine": cuisine,
        "cuisine_normalized": _normalize_cuisine(cuisine),
        "difficulty": difficulty,
        "diet": diet,
        "steps": steps,
    }


_FALLBACK_RECIPE_DATA = [
    _make_fallback_recipe(
        "Tomato Onion Curry",
        ["tomato", "onion", "garlic", "oil", "salt"],
        "Indian", "Easy",
        [
            "Chop tomato and onion.",
            "Heat oil in a pan.",
            "Saute onion and garlic.",
            "Add tomato and cook until soft.",
            "Season and simmer for 5 minutes."
        ]
    ),
    _make_fallback_recipe(
        "Garlic Potato Fry",
        ["potato", "garlic", "oil", "salt", "pepper"],
        "Indian", "Easy",
        [
            "Boil or parboil potatoes.",
            "Heat oil in a pan.",
            "Add garlic and potato.",
            "Season with salt and pepper.",
            "Roast until golden."
        ]
    ),
    _make_fallback_recipe(
        "Vegetable Stir Fry",
        ["onion", "garlic", "carrot", "beans", "soy sauce"],
        "Asian", "Medium",
        [
            "Slice all vegetables evenly.",
            "Heat a pan or wok.",
            "Add garlic and onion first.",
            "Add remaining vegetables and stir fry.",
            "Finish with soy sauce."
        ]
    ),
]

# ----- GET RECIPES (from CSV or fallback) -----
def _get_recipe_data():
    data = _load_recipes_from_csv()
    return data if data else _FALLBACK_RECIPE_DATA

# ----- SIMPLE RECIPE BUILDER (legacy, used by some tests) -----
def build_recipe(ingredients):
    recs = _get_recipe_data()
    ingredients_set = set(i.lower() for i in ingredients)
    if "tomato" in ingredients_set and "onion" in ingredients_set:
        return "Tomato Onion Curry"
    if "potato" in ingredients_set and "garlic" in ingredients_set:
        return "Garlic Potato Fry"
    return "Mixed Vegetable Dish"

# ----- COMMON ITEMS MANY PEOPLE HAVE -----
# We treat these as "pantry staples" — separate from "things to buy"
PANTRY_STAPLES = {"oil", "salt", "pepper", "soy sauce"}

# ----- PROTEINS THAT ARE NOT INTERCHANGEABLE -----
# Chicken and mutton are different! If user has mutton, don't show chicken recipes
MAIN_PROTEINS = {"chicken", "fish", "egg", "prawn", "mutton", "beef", "lamb", "pork", "shrimp"}

# ----- CHECK: DOES RECIPE NEED A PROTEIN USER DOESN'T HAVE? -----
# Example: recipe needs chicken, user has mutton → return True (exclude this recipe)
def _recipe_requires_protein_user_lacks(recipe_ings, user_ings):
    recipe_proteins = recipe_ings & MAIN_PROTEINS
    user_proteins = user_ings & MAIN_PROTEINS
    if not recipe_proteins:
        return False  # Vegetarian recipe — no protein check needed
    missing_proteins = recipe_proteins - user_ings
    return bool(missing_proteins)

# ----- MAIN FUNCTION: RECOMMEND RECIPES -----
# Returns two lists: "you_can_make" and "close_add_few"
# Diet is inferred from ingredients; cuisine matching is normalized (case-insensitive).
def recommend_recipes(ingredients, cuisine="Any", diet="None"):
    ingredients_set = set(i.lower() for i in ingredients if i)
    RECIPE_DATA = _get_recipe_data()
    cuisine_filter = _normalize_cuisine(cuisine) if cuisine and cuisine != "Any" else "Any"

    you_can_make = []
    close_add_few = []

    for recipe in RECIPE_DATA:
        # Skip if cuisine doesn't match (case-insensitive, handles South/North Indian)
        recipe_cuisine = recipe.get("cuisine_normalized") or _normalize_cuisine(recipe.get("cuisine", ""))
        if cuisine_filter != "Any" and recipe_cuisine != cuisine_filter:
            continue
        # Skip if diet doesn't match (e.g. user chose Vegan, recipe has egg)
        if diet != "None" and diet not in recipe["diet"]:
            continue

        recipe_ings = set(recipe["ingredients"])
        # Skip if recipe needs chicken but user has mutton (avoid confusion)
        if _recipe_requires_protein_user_lacks(recipe_ings, ingredients_set):
            continue

        # Count how many ingredients overlap (user has AND recipe needs)
        overlap_set = ingredients_set.intersection(recipe_ings)
        overlap = len(overlap_set)
        missing = recipe_ings - ingredients_set
        missing_count = len(missing)

        # Need at least 2 overlapping ingredients to show the recipe
        if overlap < 2:
            continue

        # What fraction of the recipe's ingredients does the user have?
        total = len(recipe_ings)
        overlap_ratio = overlap / total if total else 0

        # Add metadata so the app can show "You have 3 of 5 ingredients"
        recipe_with_meta = dict(recipe)
        recipe_with_meta["overlap"] = overlap
        recipe_with_meta["missing_count"] = missing_count
        recipe_with_meta["missing_ingredients"] = sorted(missing)

        # Tier 1: user has 50% or more → "You can make"
        if overlap_ratio >= 0.5:
            you_can_make.append((overlap, -missing_count, recipe_with_meta))
        # Tier 2: user has 2+ but less than 50% → "Close — add a few"
        else:
            close_add_few.append((overlap, -missing_count, recipe_with_meta))

    # Sort by: most overlap first, then fewest missing ingredients
    you_can_make.sort(key=lambda x: (x[0], x[1]), reverse=True)
    close_add_few.sort(key=lambda x: (x[0], x[1]), reverse=True)

    return {
        "you_can_make": [m[2] for m in you_can_make],
        "close_add_few": [m[2] for m in close_add_few],
    }
