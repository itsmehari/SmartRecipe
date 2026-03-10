import csv
from pathlib import Path

def _load_recipes_from_csv():
    """Load recipe data from data/recipes.csv. Returns list of recipe dicts or None if file missing."""
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
            ingredients = [i.strip().lower() for i in row.get("ingredients", "").split(",") if i.strip()]
            diet_str = row.get("diet", "")
            diet = [d.strip() for d in diet_str.split(",") if d.strip()] if diet_str else []
            steps_str = row.get("steps", "")
            steps = [s.strip() for s in steps_str.split("|") if s.strip()] if steps_str else []
            recipes.append({
                "name": row.get("recipe_name", "").strip(),
                "ingredients": ingredients,
                "cuisine": row.get("cuisine", "").strip(),
                "difficulty": row.get("difficulty", "").strip(),
                "diet": diet,
                "steps": steps if steps else ["See recipe instructions."],
            })
    return recipes if recipes else None

# Fallback hardcoded data if CSV missing or empty
_FALLBACK_RECIPE_DATA = [
    {
        "name": "Tomato Onion Curry",
        "ingredients": ["tomato", "onion", "garlic", "oil", "salt"],
        "cuisine": "Indian",
        "difficulty": "Easy",
        "diet": ["Vegetarian", "Jain"],
        "steps": [
            "Chop tomato and onion.",
            "Heat oil in a pan.",
            "Saute onion and garlic.",
            "Add tomato and cook until soft.",
            "Season and simmer for 5 minutes."
        ]
    },
    {
        "name": "Garlic Potato Fry",
        "ingredients": ["potato", "garlic", "oil", "salt", "pepper"],
        "cuisine": "Indian",
        "difficulty": "Easy",
        "diet": ["Vegetarian", "Vegan", "Jain", "High Protein"],
        "steps": [
            "Boil or parboil potatoes.",
            "Heat oil in a pan.",
            "Add garlic and potato.",
            "Season with salt and pepper.",
            "Roast until golden."
        ]
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["onion", "garlic", "carrot", "beans", "soy sauce"],
        "cuisine": "Asian",
        "difficulty": "Medium",
        "diet": ["Vegetarian", "Vegan"],
        "steps": [
            "Slice all vegetables evenly.",
            "Heat a pan or wok.",
            "Add garlic and onion first.",
            "Add remaining vegetables and stir fry.",
            "Finish with soy sauce."
        ]
    }
]

def _get_recipe_data():
    data = _load_recipes_from_csv()
    return data if data else _FALLBACK_RECIPE_DATA

def build_recipe(ingredients):
    recs = _get_recipe_data()
    ingredients_set = set(i.lower() for i in ingredients)
    if "tomato" in ingredients_set and "onion" in ingredients_set:
        return "Tomato Onion Curry"
    if "potato" in ingredients_set and "garlic" in ingredients_set:
        return "Garlic Potato Fry"
    return "Mixed Vegetable Dish"

# Ingredients many users already have; recipes can assume these
PANTRY_STAPLES = {"oil", "salt", "pepper", "soy sauce"}

def recommend_recipes(ingredients, cuisine="Any", diet="None"):
    """
    Returns dict with two tiers:
    - you_can_make: recipes where user has 50%+ of ingredients (strict, practical)
    - close_add_few: recipes with 2+ overlap but below 50% (exploratory)
    Each recipe includes overlap, missing_count, missing_ingredients for display.
    """
    ingredients = set(ingredients)
    RECIPE_DATA = _get_recipe_data()
    cuisine_filter = cuisine
    if cuisine in ("South Indian", "North Indian"):
        cuisine_filter = "Indian"

    you_can_make = []
    close_add_few = []

    for recipe in RECIPE_DATA:
        if cuisine_filter != "Any" and recipe["cuisine"] != cuisine_filter:
            continue
        if diet != "None" and diet not in recipe["diet"]:
            continue

        recipe_ings = set(recipe["ingredients"])
        overlap_set = ingredients.intersection(recipe_ings)
        overlap = len(overlap_set)
        missing = recipe_ings - ingredients
        missing_count = len(missing)

        if overlap < 2:
            continue

        total = len(recipe_ings)
        overlap_ratio = overlap / total if total else 0

        recipe_with_meta = dict(recipe)
        recipe_with_meta["overlap"] = overlap
        recipe_with_meta["missing_count"] = missing_count
        recipe_with_meta["missing_ingredients"] = sorted(missing)

        # Tier 1: user has 50%+ of recipe ingredients
        if overlap_ratio >= 0.5:
            you_can_make.append((overlap, -missing_count, recipe_with_meta))
        else:
            close_add_few.append((overlap, -missing_count, recipe_with_meta))

    you_can_make.sort(key=lambda x: (x[0], x[1]), reverse=True)
    close_add_few.sort(key=lambda x: (x[0], x[1]), reverse=True)

    return {
        "you_can_make": [m[2] for m in you_can_make],
        "close_add_few": [m[2] for m in close_add_few],
    }
