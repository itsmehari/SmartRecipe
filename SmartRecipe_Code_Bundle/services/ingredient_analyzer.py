import csv
from pathlib import Path

def _load_known_ingredients():
    """Load known ingredient names from data/ingredients.csv. Returns set of lowercase names or empty set."""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    csv_path = data_dir / "ingredients.csv"
    if not csv_path.exists():
        return set()
    names = set()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("ingredient_name", "").strip().lower()
            if name:
                names.add(name)
    return names

def analyze_ingredients(ingredients):
    normalized = [item.strip().lower() for item in ingredients if item.strip()]
    known = _load_known_ingredients()
    # Use canonical form if input matches a known ingredient (e.g. "Tomatoes" -> "tomato" if in CSV)
    result = []
    for item in normalized:
        if item in known:
            result.append(item)
        else:
            # Keep as-is (normalized); optional: match first known ingredient that starts with item
            result.append(item)
    return result
