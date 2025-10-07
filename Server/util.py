import pickle as pkl
import json
import numpy as np
from pathlib import Path
_data_columns = None
_locations = None
_model = None

BASE_DIR = Path(__file__).parent.parent
columns_path = BASE_DIR / "model" / "columns.json"
model_path = BASE_DIR / "model" / "bengaluru_house_price_model.pkl"
def get_location_names():
    ''' Get the location names'''
    return _locations


def load_artifacts():
    ''' Load the artifacts from the model folder'''
    try:
        with open(columns_path, "rb") as file:
            global _data_columns
            _data_columns = json.load(file)['data_columns']
            global _locations
            _locations = _data_columns[3:]
        with open(model_path, "rb") as file:
            global _model
            _model = pkl.load(file)
        print("artifacts loaded")
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        raise e

def get_prediction_price(bath, bhk, sqft, location):
    ''' Get the prediction of the house price'''
    return predict_price(bath, bhk, sqft, location)


def predict_price(bath, bhk, area_sqft, location):
    ''' Predict the price based on the model'''
    try:
        loc_index = _data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(_data_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = area_sqft
    if loc_index >= 0:
        x[loc_index] = 1
    return round(_model.predict([x])[0],2)


if __name__ == "__main__":
    ''' For testing purpose'''
    load_artifacts()
    print(get_location_names)
    print(get_prediction_price(3, 3, 1000, "1st Phase JP Nagar"))
    print(get_prediction_price(2, 2, 1000, "1st Phase JP Nagar"))
    print(get_prediction_price(2, 2, 1000, "Ejipura"))