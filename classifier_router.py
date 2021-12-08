from pathlib import Path
from joblib import load
import numpy as np

from fastapi import APIRouter
from starlette.responses import JSONResponse

from .schemas import Wine


ROOT_DIR = Path(__file__).parent
scaler = load(ROOT_DIR/"artifacts/scaler.joblib")
model = load(ROOT_DIR/"artifacts/model.joblib")
class_mapping = {0: "Bad", 1: "Good"}


router = APIRouter()


@router.post("/predict")
async def predict(sample: Wine):
    sample_dict = sample.dict()
    features = np.array(list(sample_dict.values())).reshape(1, -1)
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    predict_prob = model.predict_proba(scaled_features)[0]
    d = dict()
    d['class_prediction'] = class_mapping[prediction]
    d['prediction'] = int(prediction)
    d['class_prob'] = float(predict_prob[prediction] * 100)
    return JSONResponse({"prediction": d})
