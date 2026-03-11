"""
SmartRecipe — Main Application
==============================
This is the main screen of the SmartRecipe app. It lets users:
1. Type in the ingredients they have
2. Choose diet and cuisine filters
3. See recipes they can make, plus nutrition and shopping lists

Written in simple terms so anyone reading the code can understand what each part does.
"""

# ----- BRING IN THE HELPER TOOLS -----
# These are like "assistants" — each one does a specific job for the app
import streamlit as st
# Takes what the user types and cleans it up, fixes typos (e.g. "tamato" -> "tomato")
from services.ingredient_analyzer import analyze_ingredients
# Finds which recipes match the user's ingredients
from services.recipe_engine import recommend_recipes
# Figures out roughly how many calories, protein, etc. each recipe has
from services.nutrition_engine import estimate_nutrition
# Makes a list of what the user still needs to buy for a recipe
from services.shopping_list import generate_shopping_list
# Try to use the "split" version — separates "pantry items" (oil, salt) from "things to buy"
try:
    from services.shopping_list import generate_shopping_list_split
except ImportError:
    # If that doesn't exist (old version), we create our own simple version here
    _PANTRY = {"oil", "salt", "pepper", "soy sauce"}
    def generate_shopping_list_split(avail, rec):
        missing = generate_shopping_list(avail, rec)
        pantry = [m for m in missing if m.lower() in _PANTRY]
        to_buy = [m for m in missing if m.lower() not in _PANTRY]
        return {"pantry": pantry, "to_buy": to_buy}
# Checks if the user chose "Vegan" but typed "egg" — warns them
from services.diet_validator import get_conflicting_ingredients, get_diet_guidance

# ----- SET UP THE PAGE -----
st.set_page_config(page_title="SmartRecipe", layout="wide")
st.title("SmartRecipe")
st.caption("AI Ingredient-Driven Cooking Engine")
# Important message: we're not doctors or dietitians, this is just suggestions
st.info("This system provides recipe suggestions and is not a substitute for professional nutritional advice.")

# ----- SIDEBAR (the left panel) -----
# Everything below runs "inside" the sidebar
with st.sidebar:
    # Tell new users the 3 simple steps
    st.header("How to use")
    st.markdown("""
    1. **Ingredient Entry** — Enter what you have
    2. Click **Analyze Ingredients**
    3. **Recipe Dashboard** — See your matches
    """)
    st.divider()

    # A collapsible box that explains what each diet filter means
    with st.expander("About diet filters", expanded=False):
        st.markdown("""
        - **Vegetarian** — Excludes meat, fish, seafood
        - **Vegan** — Excludes all animal products (meat, fish, eggs, dairy, honey)
        - **Non-Vegetarian** — Includes chicken, fish, egg, prawn
        - **Jain** — Excludes meat, fish, eggs, and root vegetables (onion, garlic, potato, carrot)
        - **High Protein** — No exclusions (veg and non-veg)

        *If your ingredients don't match your diet, we'll warn you — but we won't block you.*
        """)
    st.divider()

    # The three dropdowns/number box that let users filter results
    st.header("Filters")
    diet = st.selectbox("Diet Type", ["None", "Vegetarian", "Non-Vegetarian", "Vegan", "Jain", "High Protein"], help="Filter recipes by diet")
    cuisine = st.selectbox("Cuisine Preference", ["Any", "Indian", "South Indian", "North Indian", "Italian", "Asian"], help="Filter by cuisine style")
    servings = st.number_input("Servings", min_value=1, max_value=10, value=2, help="For nutrition per serving")

# ----- CREATE TWO TABS -----
# Tab 1 = where you type ingredients
# Tab 2 = where you see the recipes
tab1, tab2 = st.tabs(["1. Ingredient Entry", "2. Recipe Dashboard"])

# ========== TAB 1: WHERE USER TYPES INGREDIENTS ==========
with tab1:
    st.subheader("Step 1: Enter your available ingredients")
    st.markdown("Type the ingredients you have in your kitchen, separated by commas. You can use any format (e.g. *tomato*, *onions*, *garlic*).")

    # Big text box where user types: tomato, onion, garlic, etc.
    ingredients_input = st.text_area(
        "Ingredients (comma-separated)",
        placeholder="e.g. tomato, onion, garlic, potato, carrot, beans",
        help="Enter at least 2–3 ingredients for better recipe matches"
    )

    # When user clicks this button, we process their ingredients
    if st.button("Analyze Ingredients", type="primary"):
        # First check: did they type anything at all?
        if not ingredients_input or not ingredients_input.strip():
            st.warning("Please enter at least one ingredient.")
        else:
            # Send the list to our analyzer — it fixes typos and returns clean list
            ingredients, corrections = analyze_ingredients(ingredients_input.split(","))
            # Save in memory so Tab 2 can use it when user switches tabs
            st.session_state["ingredients"] = ingredients
            st.session_state["diet_at_analyze"] = diet

            # If we fixed any typos (e.g. tamato -> tomato), show them what we did
            if corrections:
                st.success("**We corrected some ingredients:** " + " | ".join(f"*{orig}* → **{fix}**" for orig, fix in corrections))

            # Check: did user pick "Vegan" but type "egg"? Or "Vegetarian" but type "chicken"?
            conflicting = get_conflicting_ingredients(ingredients, diet) if diet != "None" else []
            if conflicting:
                # Show a warning but don't stop them — they can still see recipes
                st.warning(f"**Diet mismatch:** You selected **{diet}** (typically {get_diet_guidance(diet)}), but you entered: **{', '.join(conflicting)}**.")
                st.markdown("**What to do:**")
                st.markdown("- Remove these ingredients and re-analyze, or")
                st.markdown("- Change **Diet Type** to **None** in the sidebar to see recipes with these ingredients.")
                st.info("Your ingredients are saved. Go to **Recipe Dashboard** — you can switch the diet filter in the sidebar anytime.")
            elif not corrections:
                # All good — no typos, no diet clash
                st.success("Ingredients analyzed successfully. Your list is ready.")
                if diet != "None":
                    st.caption(f"Diet filter **{diet}** applied — recipes will match this diet.")

            # Always show the final list we're using, and remind them to go to Tab 2
            st.markdown("**Ingredients we found:** " + ", ".join(f"`{i}`" for i in ingredients))
            st.info("**Next step:** Go to the **Recipe Dashboard** tab (above) to see recipe recommendations based on these ingredients and your filters.")

# ========== TAB 2: WHERE USER SEES RECIPES ==========
with tab2:
    st.subheader("Step 2: View your recommended recipes")
    # Get the ingredients we saved from Tab 1 (or empty if they haven't done Tab 1 yet)
    ingredients = st.session_state.get("ingredients", [])

    if not ingredients:
        # They jumped straight to this tab — tell them to go back and add ingredients first
        st.warning("**Start here first:** You haven't entered any ingredients yet.")
        st.markdown("Go to the **Ingredient Entry** tab, enter what you have (e.g. *tomato, onion, garlic*), then click **Analyze Ingredients**. After that, come back here to see your recipes.")
        st.divider()
        st.caption("Tip: Enter at least 2 ingredients for best results.")
    else:
        # Show diet conflict warning here too (in case they changed diet after analyzing)
        conflicting = get_conflicting_ingredients(ingredients, diet) if diet != "None" else []
        if conflicting:
            st.warning(f"**Diet mismatch:** You selected **{diet}** (typically {get_diet_guidance(diet)}), but your ingredients include: **{', '.join(conflicting)}**.")
            st.markdown("Recipes below are filtered by diet — you may see fewer or no matches.")
            st.caption("💡 Set **Diet Type** to **None** in the sidebar to see recipes that use these ingredients.")

        # Ask the recipe engine: which recipes match? Split into "you can make" vs "close"
        result = recommend_recipes(ingredients, cuisine=cuisine, diet=diet)
        you_can_make = result["you_can_make"]
        close_add_few = result["close_add_few"]
        total = len(you_can_make) + len(close_add_few)

        if total == 0:
            # No recipes matched — give them tips
            st.warning("No recipes match your ingredients and filters.")
            if conflicting:
                st.info("**Quick fix:** Set **Diet Type** to **None** in the sidebar to see recipes that use " + ", ".join(f"*{c}*" for c in conflicting) + ".")
            st.markdown("**What to try:**")
            st.markdown("1. Set **Cuisine** to **Any** and **Diet** to **None** in the sidebar to see all matches")
            st.markdown("2. Add more ingredients in **Ingredient Entry** (e.g. *oil*, *salt*, *potato*, *carrot*, *beans*)")
            st.caption("Available cuisines: Indian, Asian, Italian. Diets: Vegetarian, Non-Vegetarian, Vegan, Jain, High Protein.")
        else:
            # We found recipes — show success message and the two sections
            st.success(f"Found **{total}** recipe(s). Recipes you can make with your ingredients are listed first.")
            st.caption("**You can make** = you have 50%+ of ingredients. **Close** = add a few items to try.")

            # Helper function: draw one recipe card (name, steps, nutrition, shopping list)
            def render_recipe(recipe, badge=""):
                st.markdown("---")
                st.markdown(f"### {recipe['name']}" + (f" {badge}" if badge else ""))

                # Three small columns: cuisine | difficulty | how many ingredients they have
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    st.markdown("**Cuisine:** " + recipe["cuisine"])
                with col2:
                    st.markdown("**Difficulty:** " + recipe["difficulty"])
                with col3:
                    st.markdown(f"**You have:** {recipe.get('overlap', 0)} of {len(recipe['ingredients'])} ingredients")

                # Expandable box: full list of ingredients
                with st.expander("What you need", expanded=True):
                    st.markdown(", ".join(recipe["ingredients"]))

                # Expandable box: cooking steps
                with st.expander("How to make it"):
                    for i, step in enumerate(recipe["steps"], start=1):
                        st.markdown(f"{i}. {step}")

                # Nutrition: calories, protein, carbs, fat (per serving)
                st.markdown("**Estimated nutrition (per serving, approximate):**")
                nutrition = estimate_nutrition(recipe["ingredients"], servings=servings)
                n1, n2, n3, n4 = st.columns(4)
                n1.metric("Calories", f"{nutrition['calories']} kcal")
                n2.metric("Protein", f"{nutrition['protein']} g")
                n3.metric("Carbs", f"{nutrition['carbs']} g")
                n4.metric("Fat", f"{nutrition['fat']} g")

                # Shopping list: split into "things to buy" vs "pantry items you might already have"
                split = generate_shopping_list_split(ingredients, recipe["ingredients"])
                pantry, to_buy = split["pantry"], split["to_buy"]
                if to_buy:
                    st.warning("**To buy:** " + ", ".join(to_buy))
                if pantry:
                    st.caption("**Pantry (you may have):** " + ", ".join(pantry))
                if not to_buy and not pantry:
                    st.success("You have all the ingredients needed for this recipe.")

            # Section 1: "You can make" — user has most ingredients
            if you_can_make:
                st.markdown("#### ✓ You can make")
                for recipe in you_can_make:
                    render_recipe(recipe)

            # Section 2: "Close" — user has some, needs a few more
            if close_add_few:
                st.markdown("#### ○ Close — add a few ingredients")
                for recipe in close_add_few:
                    missing = recipe.get("missing_ingredients", [])
                    render_recipe(recipe, badge=f"_(+{len(missing)} to buy)_")
