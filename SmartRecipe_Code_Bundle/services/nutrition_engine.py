NUTRITION_DB = {
    "tomato": {"calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2},
    "onion": {"calories": 40, "protein": 1.1, "carbs": 9.3, "fat": 0.1},
    "garlic": {"calories": 149, "protein": 6.4, "carbs": 33.1, "fat": 0.5},
    "potato": {"calories": 77, "protein": 2.0, "carbs": 17.0, "fat": 0.1},
    "carrot": {"calories": 41, "protein": 0.9, "carbs": 10.0, "fat": 0.2},
    "beans": {"calories": 31, "protein": 1.8, "carbs": 7.0, "fat": 0.1},
    "oil": {"calories": 120, "protein": 0, "carbs": 0, "fat": 14},
    "salt": {"calories": 0, "protein": 0, "carbs": 0, "fat": 0},
    "pepper": {"calories": 251, "protein": 10.4, "carbs": 64.8, "fat": 3.3},
    "soy sauce": {"calories": 53, "protein": 5.6, "carbs": 6.0, "fat": 0.1},
}

def estimate_nutrition(ingredients, servings=1):
    total = {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fat": 0.0}
    for item in ingredients:
        data = NUTRITION_DB.get(item.lower())
        if data:
            for key in total:
                total[key] += data[key]
    if servings > 0:
        for key in total:
            total[key] = round(total[key] / servings, 2)
    return total
