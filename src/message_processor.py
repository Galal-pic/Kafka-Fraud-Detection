import json
import pandas as pd

def process_message(msg, model):
    value = json.loads(msg.value())
    df = pd.DataFrame([value]).replace({
        'PAYMENT': 1, 'TRANSFER': 2, 'CASH_OUT': 3,
        'CASH_IN': 4, 'DEBIT': 5, 'No': 0, 'Yes': 1
    })
    df = df.infer_objects(copy=False)
    df.drop(['nameOrig', 'nameDest', 'isFlaggedFraud'], axis=1, inplace=True)
    X = df.drop(['isFraud'], axis=1)
    prediction = model.predict(X)[0]
    return value, prediction
