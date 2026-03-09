---
marp: true
theme: default
title: SmartRecipe — Ingredient-Driven AI Cooking Engine
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  section.title { justify-content: center; }
---

<!-- _class: lead -->
# SmartRecipe
## An Ingredient-Driven AI Cooking Engine

**B.Sc. Computer Science — Final Year Project**  
**Dhanraj Baid Jain College (Autonomous)**  
Thoraipakkam, Chennai – 600097

*[Your Name] | [Roll No.] | Guide: [Guide Name]*

---
# Contents
- Introduction & Problem Statement
- Objectives
- System Study
- Requirements & Technology Stack
- System Design
- Implementation
- Results & Discussion
- Limitations & Future Work
- Conclusion

---
# Introduction
- **Problem:** People have ingredients at home but don’t know what to cook.
- Traditional apps need a dish name first; they don’t start from “what I have.”
- **SmartRecipe** starts from **available ingredients** and suggests recipes.
- Uses simple AI/analysis: ingredient matching, diet filters, nutrition estimates, shopping list.

---
# Problem Statement
- Existing platforms: search by dish name, not by ingredients.
- Users often buy extra groceries and waste food.
- Little support for **diet** (vegetarian, vegan, Jain) and **cuisine** (Indian, Asian, etc.).
- **Goal:** A system that takes an ingredient list and suggests suitable recipes with filters and basic nutrition.

---
# Objectives
- Accept ingredient input from the user.
- Analyse compatibility and suggest recipe combinations.
- Apply **diet** (Vegetarian, Vegan, Jain, High Protein) and **cuisine** filters.
- Estimate **approximate nutrition** (calories, protein, carbs, fat).
- Show **missing ingredients** (shopping list) for chosen recipes.
- Provide an **interactive dashboard** (Streamlit).

---
# System Study — Existing Systems
- **Static recipe sites:** Search by dish name only.
- **Ingredient-based apps:** Often simple keyword match, no smart filtering.
- **Meal planners:** Plan ahead; don’t suggest from “what I have now.”
- **Limitation:** None of them fully combine ingredient-driven search + diet + cuisine + nutrition in one flow.

---
# Proposed Solution: SmartRecipe
- **Input:** Comma-separated ingredients (e.g. tomato, onion, garlic).
- **Processing:** Normalise ingredients, load recipes from CSV, match by overlap.
- **Filters:** Diet type, cuisine preference, number of servings.
- **Output:** Recommended recipes, steps, estimated nutrition, missing-ingredient list.

---
# Requirements
**Hardware:** PC with 4 GB+ RAM, 5 GB free storage.  
**Software:** Python 3.9+, Streamlit, Pandas, NumPy, Scikit-learn.  
**Data:** CSV files for ingredients and recipes (used in current implementation).

---
# Technology Stack
| Layer      | Technology        |
|-----------|--------------------|
| UI        | Streamlit          |
| Backend   | Python 3           |
| Data      | CSV (recipes, ingredients) |
| Libraries | Pandas, NumPy, Scikit-learn |

---
# System Architecture
1. **Input:** User enters ingredients; selects diet, cuisine, servings.
2. **Processing:** Ingredient analyser → Recipe engine (load from CSV, match, filter).
3. **Services:** Nutrition engine (estimate), Shopping list (missing items).
4. **Output:** Recipe dashboard with name, steps, nutrition, missing ingredients.

---
# Implementation — Modules
- **ingredient_analyzer.py** — Normalise and clean ingredient list.
- **recipe_engine.py** — Load recipes from CSV; recommend by overlap + filters.
- **nutrition_engine.py** — Estimate calories, protein, carbs, fat per serving.
- **shopping_list.py** — List ingredients needed but not available.
- **app.py** — Streamlit UI: tabs (Ingredient Entry, Recipe Dashboard), sidebar filters.

---
# Implementation — Data Flow
- User types ingredients → **Analyse** → Stored in session.
- User opens Recipe Dashboard → **Recommend** (diet/cuisine applied).
- For each recipe: **Estimate nutrition** (per serving), **Generate shopping list** (missing items).
- All data driven by **data/recipes.csv** and **data/ingredients.csv**.

---
# Results — Sample Run
**Input:** Tomato, Onion, Garlic  
**Output examples:** Tomato Onion Curry, Vegetable Stir Fry.  
**Nutrition (approx.):** Calories ~220 kcal, Protein ~8 g, Carbs ~30 g.  
**Dashboard shows:** Recipe name, cuisine, difficulty, ingredients, steps, nutrition, missing ingredients.

---
# Results — Performance
- **Response time:** Recommendations in a few seconds.
- **Usability:** Simple Streamlit interface for non-technical users.
- **Accuracy:** Depends on recipe data and matching rules; suitable for a prototype.

---
# Limitations
- Small recipe and ingredient datasets (CSV-based prototype).
- No image-based ingredient detection in current version.
- Nutrition is approximate, not for medical use.
- No long-term user preference learning.

---
# Future Work
- Integrate larger recipe databases.
- Mobile app / scan ingredients from phone.
- IoT: link with smart kitchen devices.
- Voice-guided cooking steps.
- Richer AI/ML for better personalisation.

---
# Conclusion
- SmartRecipe is an **ingredient-driven** recipe recommendation system.
- It uses **Python + Streamlit**, CSV data, and simple matching/filtering.
- It supports **diet and cuisine filters**, **nutrition estimates**, and **shopping list**.
- The project shows how **AI/data-driven ideas** can support daily cooking and reduce waste.

---
<!-- _class: lead -->
# Thank You

**SmartRecipe: An Ingredient-Driven AI Cooking Engine**  
B.Sc. Computer Science — Final Year Project  
Dhanraj Baid Jain College (Autonomous), Thoraipakkam, Chennai  

*Questions?*
