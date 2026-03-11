# SmartRecipe — Modules Documentation

## Invigilator Requirement: At Least 5 Modules

This document explains **how many modules** the SmartRecipe project uses and provides a **detailed explanation** of each module’s **relevance** and **functionality**.

---

## Module Count Summary

| Category | Count | Modules |
|----------|-------|---------|
| **Project Service Modules** | **5** | `ingredient_analyzer`, `recipe_engine`, `nutrition_engine`, `shopping_list`, `diet_validator` |
| **Main Application** | 1 | `app.py` |
| **Python Standard Library Modules** | 3+ | `csv`, `pathlib`, `difflib` |
| **External Libraries** | 1+ | `streamlit` |

The project uses **5 core service modules** plus the main application module, satisfying the requirement of **at least 5 modules**.

---

## 1. Project Service Modules (5 Modules)

### 1.1 `ingredient_analyzer`

**File:** `services/ingredient_analyzer.py`

**Purpose:** Cleans and corrects user-typed ingredients before any other processing.

**Functionality:**
- Fixes common typos (e.g., "tamato" → "tomato", "chiken" → "chicken")
- Handles plurals (e.g., "tomatoes" → "tomato")
- Uses fuzzy string matching (`difflib`) for similar-looking misspellings
- Loads reference ingredients from `ingredients.csv` and recipe data for validation
- Returns a corrected list and a list of corrections (so the app can show users what was fixed)

**Relevance in Project:**
- Improves recipe matching by normalizing user input
- Makes the system more user-friendly and tolerant of spelling mistakes

---

### 1.2 `recipe_engine`

**File:** `services/recipe_engine.py`

**Purpose:** Selects recipes that match the user’s ingredients and filters.

**Functionality:**
- Loads recipes from `recipes.csv` (or uses fallback data)
- Filters by **diet** (Vegetarian, Non-Vegetarian, Vegan, Jain, High Protein)
- Filters by **cuisine** (Indian, South Indian, North Indian, Italian, Asian)
- Uses **ingredient-based diet inference** (no veg recipes shown when user has non-veg ingredients)
- Enforces **cuisine normalization** (case-insensitive, South/North Indian → Indian)
- Classifies recipes into “You can make” (≥50% overlap) and “Close — add a few” (<50% overlap)
- Avoids showing recipes that require proteins the user doesn’t have (e.g., chicken recipes if user has mutton)

**Relevance in Project:**
- Core recommendation logic of the app
- Ensures diet and cuisine filters are applied correctly

---

### 1.3 `nutrition_engine`

**File:** `services/nutrition_engine.py`

**Purpose:** Estimates nutritional values per serving for each recipe.

**Functionality:**
- Keeps an internal database of approximate calories, protein, carbs, and fat per 100g for common ingredients
- Sums nutrition for all ingredients in a recipe
- Divides by the number of servings to get per-serving estimates
- Returns: calories (kcal), protein (g), carbs (g), fat (g)

**Relevance in Project:**
- Gives users an idea of the nutritional content of recipes
- Helps with diet planning and awareness

---

### 1.4 `shopping_list`

**File:** `services/shopping_list.py`

**Purpose:** Identifies ingredients the user still needs to buy for a selected recipe.

**Functionality:**
- Compares the user’s available ingredients with the recipe’s required ingredients
- Identifies **missing ingredients**
- Splits missing items into:
  - **Pantry items** (oil, salt, pepper, soy sauce) — usually already available
  - **To buy** — main ingredients to purchase

**Relevance in Project:**
- Assists users in planning grocery shopping
- Improves usability by separating pantry staples from items to buy

---

### 1.5 `diet_validator`

**File:** `services/diet_validator.py`

**Purpose:** Checks if user ingredients are consistent with the selected diet and infers recipe diets from ingredients.

**Functionality:**
- **Conflict detection:** Warns when the selected diet conflicts with typed ingredients (e.g., Vegan + egg)
- **Diet guidance:** Returns short descriptions of what each diet excludes
- **Ingredient-based diet inference:** Classifies recipes as veg/non-veg/vegan/jain from ingredients (not only CSV)
- Ensures recipes with chicken, fish, egg, etc. are never shown as Vegetarian

**Relevance in Project:**
- Improves correctness of veg/non-veg classification
- Helps users avoid unintended diet mismatches

---

## 2. Main Application Module

### 2.1 `app`

**File:** `app.py`

**Purpose:** Main entry point and web UI of the SmartRecipe application.

**Functionality:**
- Streamlit-based web interface
- Two tabs: Ingredient Entry, Recipe Dashboard
- Sidebar with diet and cuisine filters, servings
- Integrates all 5 service modules
- Displays recipes, nutrition, shopping lists, and diet warnings

**Relevance in Project:**
- Ties together all services into a single user-facing application

---

## 3. Python Standard Library Modules Used

| Module   | Used In          | Purpose                                      |
|----------|------------------|----------------------------------------------|
| `csv`    | recipe_engine, ingredient_analyzer | Read recipes.csv, ingredients.csv          |
| `pathlib`| recipe_engine, ingredient_analyzer | Locate data files across project paths     |
| `difflib`| ingredient_analyzer              | Fuzzy string matching for typo correction   |

---

## 4. External Python Libraries

| Library   | Purpose                      | File(s)   |
|-----------|-----------------------------|-----------|
| **Streamlit** | Build and run the web UI | `app.py`  |

---

## 5. Data Dependencies

- `recipes.csv` — Recipe list (name, cuisine, ingredients, steps, diet)
- `ingredients.csv` — Valid ingredient names and metadata

---

## Summary for Invigilator

The SmartRecipe project uses **5 project service modules**:

1. **ingredient_analyzer** — Input cleaning and typo correction  
2. **recipe_engine** — Recipe recommendation and filtering  
3. **nutrition_engine** — Nutrition estimation  
4. **shopping_list** — Shopping list generation  
5. **diet_validator** — Diet validation and inference  

Each module has a distinct responsibility and is integrated into the main application (`app.py`), meeting the requirement of **at least 5 modules**.
