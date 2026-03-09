import streamlit as st
from services.ingredient_analyzer import analyze_ingredients
from services.recipe_engine import build_recipe, recommend_recipes
from services.nutrition_engine import estimate_nutrition
from services.shopping_list import generate_shopping_list

st.set_page_config(page_title="SmartRecipe", layout="wide")

st.title("SmartRecipe")
st.caption("AI Ingredient-Driven Cooking Engine")
st.info("This system provides recipe suggestions and is not a substitute for professional nutritional advice.")

with st.sidebar:
    st.header("Filters")
    diet = st.selectbox("Diet Type", ["None", "Vegetarian", "Vegan", "Jain", "High Protein"])
    cuisine = st.selectbox("Cuisine Preference", ["Any", "Indian", "South Indian", "North Indian", "Italian", "Asian"])
    servings = st.number_input("Servings", min_value=1, max_value=10, value=2)

tab1, tab2 = st.tabs(["Ingredient Entry", "Recipe Dashboard"])

with tab1:
    st.subheader("Enter Available Ingredients")
    ingredients_input = st.text_area(
        "Ingredients (comma-separated)",
        placeholder="tomato, onion, garlic, potato"
    )
    if st.button("Analyze Ingredients"):
        ingredients = analyze_ingredients(ingredients_input.split(","))
        st.session_state["ingredients"] = ingredients
        st.success("Ingredients analyzed successfully.")
        st.write("Normalized Ingredients:", ingredients)

with tab2:
    st.subheader("Recommended Recipes")
    ingredients = st.session_state.get("ingredients", [])
    if ingredients:
        recipes = recommend_recipes(ingredients, cuisine=cuisine, diet=diet)
        if recipes:
            for recipe in recipes:
                st.markdown(f"### {recipe['name']}")
                st.write("Cuisine:", recipe["cuisine"])
                st.write("Difficulty:", recipe["difficulty"])
                st.write("Ingredients:", ", ".join(recipe["ingredients"]))
                st.write("Steps:")
                for i, step in enumerate(recipe["steps"], start=1):
                    st.write(f"{i}. {step}")
                nutrition = estimate_nutrition(recipe["ingredients"], servings=servings)
                st.write("Estimated Nutrition (approximate per serving):", nutrition)
                shopping = generate_shopping_list(ingredients, recipe["ingredients"])
                st.write("Missing Ingredients:", shopping if shopping else "None")
                st.divider()
        else:
            st.warning("No matching recipes found for the selected filters.")
    else:
        st.warning("Enter ingredients first in the Ingredient Entry tab.")
