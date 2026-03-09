# SmartRecipe

SmartRecipe is an academic Streamlit project that recommends recipes from available ingredients.

## Features
- Ingredient normalization
- Recipe recommendation
- Dietary and cuisine filters
- Nutritional estimation
- Shopping list generation

## Run locally

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud
1. Push this project to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**.
4. **Repository:** select your repo (e.g. `yourusername/SmartRecipe`).
5. **Branch:** `main` (or your default branch).
6. **Main file path:** `SmartRecipe_Code_Bundle/app.py`
7. **App URL:** (optional) choose a subdomain.
8. Click **Deploy**.
