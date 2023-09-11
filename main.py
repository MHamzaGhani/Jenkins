from fastapi import FastAPI, File, UploadFile
import pandas as pd
import numpy as np
from prophet import Prophet
import joblib
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get/")
async def get_result():
        return "Choosni is a ditcher"


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Attempt to read the CSV file
        df = pd.read_csv(file.file)
        
        # Perform your data processing
        df = df[['Date','Primary Type','Description','Arrest','Domestic']]
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M')
        df.index = pd.DatetimeIndex(df['Date'])
        df.drop("Date", axis=1, inplace=True)
        model_data = df.resample('M').size().reset_index()
        model_data.rename(columns={"Date":"ds",0:"y"}, inplace=True)
        model = Prophet()
        model.fit(model_data)
        joblib.dump(model, "trained_prophet_model.pkl")
        
        return JSONResponse(content={"message": "Model trained and saved."})
    except ParserError as e:
        # Handle the parsing error
        return JSONResponse(content={"error": f"Error parsing CSV file: {str(e)}"})




@app.post("/predict/")
async def predict(months:int):
        model = joblib.load("trained_prophet_model.pkl")
        future=model.make_future_dataframe(periods=months, freq='MS')
        forecast=model.predict(future)
        return forecast.sort_values("ds")["yhat"].tail(months)





