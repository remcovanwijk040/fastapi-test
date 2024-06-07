import uvicorn
from fastapi import FastAPI
import joblib
from Purchase import Purchase

app = FastAPI()
# joblib_in = open("car-recommender.joblib","rb")

# load
model = joblib.load("classifier:0.1.0.pkl")



@app.get('/')
def index():
    return {'message': 'Purchase esimator'}

@app.post('/purchase/predict')
def predict_purchase(data:Purchase):
    data = data.dict()
    age=data['age']
    EstimatedSalary=data['EstimatedSalary']

    prediction = model.predict([[age, EstimatedSalary]])
    
    if prediction[0] == 0:
        return {
        'prediction': 'Not Buying'
        }
    if prediction[0] == 1:
        return {
        'prediction': 'Buying'
        }
    else:
        return {
        'prediction': 'Error'
        }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8008)
