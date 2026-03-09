# SmartRecipe

**An Ingredient-Driven AI Cooking Engine** — B.Sc. Computer Science Final Year Project

Recommends recipes from available ingredients with diet/cuisine filters, nutrition estimation, and shopping list generation.

## Project Structure

```
SmartReciepie/
├── SmartRecipe_Code_Bundle/     ← Streamlit app (deploy this)
│   ├── app.py
│   ├── requirements.txt
│   ├── data/
│   ├── services/
│   └── .streamlit/
├── SmartRecipe_Project_Report.md
├── SmartRecipe_Presentation.md
└── README.md
```

## Run Locally

```bash
cd SmartRecipe_Code_Bundle
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501

## Deploy to Streamlit Cloud

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. **Repository:** your GitHub repo.
4. **Main file path:** `SmartRecipe_Code_Bundle/app.py`
5. Click **Deploy**.

## Tech Stack

- Python 3, Streamlit, Pandas, NumPy, Scikit-learn
- Data: CSV (ingredients, recipes)
