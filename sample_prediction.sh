#!/usr/bin/env bash

PORT=8000
echo "Using Port: $PORT"

curl -X 'POST' http://localhost:$PORT/predict \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "fixed_acidity": 10.4,

  "volatile_acidity": 0.26,
  
  "citric_acid": 0.48,
  
  "residual_sugar": 1.9,
  
  "chlorides": 0.066,
  
  "free_sulfur_dioxide": 6.0,
  
  "total_sulfur_dioxide": 10.0,
  
  "density": 0.99724,
  
  "ph": 3.33,
  
  "sulphates": 0.87,
  
  "alcohol": 10.9

}'