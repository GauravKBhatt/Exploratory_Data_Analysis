# Exploratory Data Analysis and Price Prediction for Cars and Bikes

This project provides a complete workflow for scraping, cleaning, analyzing, modeling, and predicting prices for car and bike listings, using both provided and scraped data from Hamrobazaar.

## Folder Structure

- `src/`
  - `data_cleaning.ipynb` — Cleaning and preprocessing for provided car data
  - `data_modeling.ipynb` — Model training for provided car data
  - `data_plotting.ipynb` — Visualization and insights for provided car data
  - `processing/`
    - `provided_data/` — Notebooks for provided car data
      - `data_cleaning.ipynb`
      - `data_modeling.ipynb`
      - `data_plotting.ipynb`
      - `model_inference.ipynb` — Predict car prices using trained model
    - `scraped_bike_data/` — Notebooks for scraped bike data
      - `data_cleaning.ipynb`
      - `data_modeling.ipynb`
      - `data_plotting.ipynb`
    - `scraped_car_data/` — Notebooks for scraped car data
      - `data_cleaning.ipynb`
      - `data_modeling.ipynb`
      - `data_plotting.ipynb`
  - `Scraping/`
    - `scraping_network.ipynb` — Scrapes car/bike listings from Hamrobazaar API

- `models/`
  - `provided_data_model.json` — Trained XGBoost model for car price prediction

- `data/`
  - `Provided/Unclean/` — Raw provided car data
  - `Provided/Clean/` — Cleaned provided car data
  - `Scraped/Unclean/` — Raw scraped car/bike data
  - `Scraped/Clean/` — Cleaned scraped car/bike data

## Main Notebooks

- **Scraping**: `src/Scraping/scraping_network.ipynb` — Scrapes car and bike listings, fetches detailed attributes, and saves to CSV.
- **Cleaning**: `src/data_cleaning.ipynb` and corresponding notebooks in `processing/` — Cleans, imputes, and encodes features for modeling.
- **Plotting**: `src/data_plotting.ipynb` and corresponding notebooks — Visualizes distributions, relationships, and insights.
- **Modeling**: `src/data_modeling.ipynb` and corresponding notebooks — Trains XGBoost regression models for price prediction.
- **Inference**: `src/processing/provided_data/model_inference.ipynb` — Loads trained model and predicts price from user input.

## Requirements

Install dependencies from `requirements.txt`:
```
pip install -r requirements.txt
```

## How to Run

1. **Scrape Data** (optional):
   - Run `src/Scraping/scraping_network.ipynb` to fetch car/bike listings from Hamrobazaar and save to CSV.

2. **Clean Data**:
   - Run the appropriate `data_cleaning.ipynb` for provided or scraped data to preprocess and save cleaned CSVs.

3. **Visualize Data**:
   - Run `data_plotting.ipynb` to generate distribution plots, boxplots, scatter plots, and heatmaps with insights.

4. **Model Training**:
   - Run `data_modeling.ipynb` to train an XGBoost regression model and save it to the `models/` folder.

5. **Model Inference**:
   - Run `model_inference.ipynb` to load the trained model and predict car prices based on user input features.

## Model Inference Instructions

- Open `src/processing/provided_data/model_inference.ipynb`.
- Enter car features as prompted (mileage, engine_cc, fuel, kilometer_run, is_automatic, is_4WD, age).
- The notebook will output the predicted car price using the trained XGBoost model.

## Notes
- All notebooks are modular and grouped by function (scraping, cleaning, plotting, modeling, inference).
- Each notebook contains markdown explanations and insights for clarity.
- The workflow supports both provided and scraped data for cars and bikes.

---

For any issues or questions, please refer to the notebook markdowns or contact the project maintainer.
