import joblib

MODEL_PATH = r"Model\XGb_model.joblib"

def load_model():
    return joblib.load(MODEL_PATH)
