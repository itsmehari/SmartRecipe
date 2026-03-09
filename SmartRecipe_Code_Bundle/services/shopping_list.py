def generate_shopping_list(available_ingredients, recipe_ingredients):
    available = set([i.strip().lower() for i in available_ingredients])
    return [item for item in recipe_ingredients if item.lower() not in available]
