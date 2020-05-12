import pickle
import json
import pandas as pd
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path(model_name = "AutoML3722eb63518") 
    model = joblib.load(model_path)

def run(rawdata):
    try:
        data = json.loads(rawdata)['text']
        result = model.predict(pd.DataFrame(data, columns = ['summary']))
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
    return json.dumps({"result": result.tolist()})
