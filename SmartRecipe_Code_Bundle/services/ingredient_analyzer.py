"""
Ingredient Analyzer — Fixes Typos and Cleans Up What the User Types
==================================================================
When users type "tamato" or "chiken", this corrects it to "tomato" and "chicken".
Uses a list of common misspellings plus fuzzy matching for similar-looking words.
Returns a clean list and which ones were corrected (so we can tell the user).
"""
import csv
from difflib import get_close_matches, SequenceMatcher
from pathlib import Path

# Dictionary of common typos: left = what user might type, right = correct word
TYPO_MAP = {
    # Tomato
    "tamato": "tomato", "tomatoes": "tomato", "tomatos": "tomato",
    "tomota": "tomato", "tamatoes": "tomato",
    # Onion
    "onino": "onion", "onions": "onion", "onionn": "onion",
    "onin": "onion", "onon": "onion",
    # Garlic
    "gralic": "garlic", "garic": "garlic", "garcl": "garlic",
    "garlc": "garlic", "garli": "garlic",
    # Potato
    "potatto": "potato", "potatos": "potato", "potatoes": "potato",
    "potaato": "potato", "patato": "potato",
    # Carrot
    "carots": "carrot", "carrots": "carrot", "carret": "carrot",
    # Chicken
    "chiken": "chicken", "chikken": "chicken", "chickn": "chicken",
    "chciken": "chicken", "chicken breast": "chicken",
    # Egg
    "eggs": "egg", "eg": "egg", "eggss": "egg",
    # Fish
    "fash": "fish", "fis": "fish", "fishh": "fish",
    # Oil
    "oli": "oil", "oile": "oil", "oill": "oil",
    # Salt
    "sal": "salt", "slt": "salt", "salt ": "salt",
    # Rice
    "rce": "rice", "ricee": "rice", "riice": "rice",
    # Butter
    "buter": "butter", "buttér": "butter", "buer": "butter",
    # Beans
    "bens": "beans", "beens": "beans", "bean": "beans",
    # Soy sauce
    "soy sause": "soy sauce", "soy souce": "soy sauce",
    "soya sauce": "soy sauce",
    # Pepper
    "peper": "pepper", "peppar": "pepper", "pepr": "pepper",
    # Basil
    "basill": "basil", "basi": "basil",
    # Pasta
    "pasta": "pasta", "pastaa": "pasta",
    # Prawn
    "prawns": "prawn", "praw": "prawn", "prwan": "prawn",
    # Mutton
    "muttom": "mutton", "muton": "mutton", "muttn": "mutton",
    # Ginger
    "ginger": "ginger", "gingerr": "ginger", "giner": "ginger",
    # Turmeric
    "tumeric": "turmeric", "turmaric": "turmeric", "tumeri": "turmeric",
    # Coconut
    "coconut": "coconut", "cocunut": "coconut", "coconet": "coconut",
    # Yogurt
    "yoghurt": "yogurt", "curd": "yogurt",
}

# Endings we remove to get base word (e.g. tomatoes -> tomato)
PLURAL_SUFFIXES = ("es", "s")

# Load valid ingredient names from ingredients.csv
def _load_known_ingredients():
    base = Path(__file__).resolve().parent.parent
    for data_dir in [base / "data", base.parent / "SmartRecipe_Code_Bundle" / "data", Path.cwd() / "data"]:
        csv_path = data_dir / "ingredients.csv"
        if csv_path.exists():
            break
    else:
        return set()
    names = set()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("ingredient_name", "").strip().lower()
            if name:
                names.add(name)
    return names

# Get every ingredient that appears in any recipe (for fuzzy matching)
def _load_recipe_ingredients():
    from .recipe_engine import _get_recipe_data
    ingredients = set()
    for recipe in _get_recipe_data():
        for ing in recipe.get("ingredients", []):
            ingredients.add(ing.strip().lower())
    return ingredients

# Combine CSV ingredients + recipe ingredients + correct spellings
def _get_reference_ingredients():
    ref = _load_known_ingredients() | _load_recipe_ingredients()
    # Add common canonical forms
    ref.update(TYPO_MAP.values())
    return list(ref)

# Find the closest matching word (e.g. "potatto" -> "potato")
def _fuzzy_match(item, reference, cutoff=0.75, n=3):
    matches = get_close_matches(item, reference, n=n, cutoff=cutoff)
    if not matches:
        return None, 0
    best = matches[0]
    ratio = SequenceMatcher(None, item, best).ratio()
    # For short words like "salt", prefer "salt" not "soy sauce"
    if len(item) <= 4 and len(best) > len(item) + 3:
        if len(matches) > 1:
            for m in matches:
                if len(m) <= len(item) + 2:
                    r = SequenceMatcher(None, item, m).ratio()
                    if r >= cutoff:
                        return m, r
    return best, ratio

# Main function: clean and correct the user's ingredient list
# Returns: (corrected list, list of (original, corrected) pairs)
def analyze_ingredients(ingredients):
    reference = _get_reference_ingredients()
    result = []
    corrections = []
    seen = set()  # So we don't add the same ingredient twice

    for raw in ingredients:
        item = raw.strip().lower()
        if not item:
            continue

        # 1. Is it in our typo dictionary? (e.g. tamato -> tomato)
        if item in TYPO_MAP:
            canonical = TYPO_MAP[item]
            if item != canonical:
                corrections.append((raw.strip(), canonical))
            if canonical not in seen:
                result.append(canonical)
                seen.add(canonical)
            continue

        # 2. Is it already a valid ingredient?
        if item in reference:
            if item not in seen:
                result.append(item)
                seen.add(item)
            continue

        # 3. Try removing plural (tomatoes -> tomato)
        base = item
        for suf in PLURAL_SUFFIXES:
            if len(item) > len(suf) + 1 and item.endswith(suf):
                candidate = item[:-len(suf)]
                if candidate in reference:
                    corrections.append((raw.strip(), candidate))
                    if candidate not in seen:
                        result.append(candidate)
                        seen.add(candidate)
                    base = None
                    break
        if base is None:
            continue

        # 4. Fuzzy match: find closest valid word (e.g. potatto -> potato)
        match, ratio = _fuzzy_match(item, reference, cutoff=0.72)
        if match and ratio >= 0.72:
            corrections.append((raw.strip(), match))
            if match not in seen:
                result.append(match)
                seen.add(match)
            continue

        # 5. Unknown ingredient: keep as-is (still useful for matching)
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result, corrections
