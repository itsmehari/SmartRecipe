import streamlit as st
from services.ingredient_analyzer import analyze_ingredients
from services.recipe_engine import recommend_recipes
from services.nutrition_engine import estimate_nutrition
from services.shopping_list import generate_shopping_list

st.set_page_config(page_title="SmartRecipe", layout="wide")

st.title("SmartRecipe")
st.caption("AI Ingredient-Driven Cooking Engine")
st.info("This system provides recipe suggestions and is not a substitute for professional nutritional advice.")

with st.sidebar:
    st.header("How to use")
    st.markdown("""
    1. **Ingredient Entry** — Enter what you have
    2. Click **Analyze Ingredients**
    3. **Recipe Dashboard** — See your matches
    """)
    st.divider()
    st.header("Filters")
    diet = st.selectbox("Diet Type", ["None", "Vegetarian", "Vegan", "Jain", "High Protein"], help="Filter recipes by diet")
    cuisine = st.selectbox("Cuisine Preference", ["Any", "Indian", "South Indian", "North Indian", "Italian", "Asian"], help="Filter by cuisine style")
    servings = st.number_input("Servings", min_value=1, max_value=10, value=2, help="For nutrition per serving")

tab1, tab2 = st.tabs(["1. Ingredient Entry", "2. Recipe Dashboard"])

with tab1:
    st.subheader("Step 1: Enter your available ingredients")
    st.markdown("Type the ingredients you have in your kitchen, separated by commas. You can use any format (e.g. *tomato*, *onions*, *garlic*).")
    ingredients_input = st.text_area(
        "Ingredients (comma-separated)",
        placeholder="e.g. tomato, onion, garlic, potato, carrot, beans",
        help="Enter at least 2–3 ingredients for better recipe matches"
    )
    if st.button("Analyze Ingredients", type="primary"):
        if not ingredients_input or not ingredients_input.strip():
            st.warning("Please enter at least one ingredient.")
        else:
            ingredients = analyze_ingredients(ingredients_input.split(","))
            st.session_state["ingredients"] = ingredients
            st.success("Ingredients analyzed successfully. Your list is ready.")
            st.markdown("**Ingredients we found:** " + ", ".join(f"`{i}`" for i in ingredients))
            st.info("**Next step:** Go to the **Recipe Dashboard** tab (above) to see recipe recommendations based on these ingredients and your filters.")

with tab2:
    st.subheader("Step 2: View your recommended recipes")
    ingredients = st.session_state.get("ingredients", [])

    if not ingredients:
        st.warning("**Start here first:** You haven't entered any ingredients yet.")
        st.markdown("Go to the **Ingredient Entry** tab, enter what you have (e.g. *tomato, onion, garlic*), then click **Analyze Ingredients**. After that, come back here to see your recipes.")
        st.divider()
        st.caption("Tip: Enter at least 2 ingredients for best results.")
    else:
        recipes = recommend_recipes(ingredients, cuisine=cuisine, diet=diet)

        if not recipes:
            st.warning("No recipes match your ingredients and filters.")
            st.markdown("Try one of these:")
            st.markdown("- Change **Diet** or **Cuisine** filters in the sidebar (e.g. select *Any* and *Any*)")
            st.markdown("- Add more ingredients in **Ingredient Entry** (e.g. *oil*, *salt*, *pepper*)")
        else:
            st.success(f"Found **{len(recipes)}** recipe(s) you can make. Scroll down to see details.")
            st.caption("Each recipe shows: ingredients needed, steps, estimated nutrition, and missing items to buy.")

            for idx, recipe in enumerate(recipes):
                st.markdown("---")
                st.markdown(f"### {recipe['name']}")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Cuisine:** " + recipe["cuisine"])
                with col2:
                    st.markdown("**Difficulty:** " + recipe["difficulty"])

                with st.expander("What you need", expanded=True):
                    st.markdown(", ".join(recipe["ingredients"]))

                with st.expander("How to make it"):
                    for i, step in enumerate(recipe["steps"], start=1):
                        st.markdown(f"{i}. {step}")

                st.markdown("**Estimated nutrition (per serving, approximate):**")
                nutrition = estimate_nutrition(recipe["ingredients"], servings=servings)
                n1, n2, n3, n4 = st.columns(4)
                n1.metric("Calories", f"{nutrition['calories']} kcal")
                n2.metric("Protein", f"{nutrition['protein']} g")
                n3.metric("Carbs", f"{nutrition['carbs']} g")
                n4.metric("Fat", f"{nutrition['fat']} g")

                shopping = generate_shopping_list(ingredients, recipe["ingredients"])
                if shopping:
                    st.warning("**Items to buy:** " + ", ".join(shopping))
                else:
                    st.success("You have all the ingredients needed for this recipe.")
