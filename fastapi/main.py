import uvicorn
import pickle
import tensorflow
from tensorflow import keras
import pandas as pd
from fastapi import FastAPI

from pydantic import BaseModel

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
     "http://localhost:8000",
     "http://localhost:4200",
     "http://127.0.0.1:8000/prediction",
 ]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )


#load the model     
model = keras.models.load_model('path/model.h5')

#load the Tokenizer 
with open('path/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

@app.get('/')

def index():

    return {'message': 'This is the homepage of the API '}

@app.post('/prediction')


def prediction(data: str):
    global model

    sentiment_classes = {1: "Negative", 0: "Positive"}
    # Transforms text to a sequence of integers using a tokenizer object
    xt = tokenizer.texts_to_sequences([data])
    # Pad sequences to the same length
    xt = pad_sequences(xt, maxlen=200)
    # Do the prediction using the loaded model
    prediction = int(model.predict(xt).round().item())
    # Print the predicted sentiment
    result = {sentiment_classes[prediction]}
    return result
    


if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)