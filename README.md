# Google Data Analysis Assignment

## Student Details
Name: M. Abdullah Ali  
SAP ID: 79209  
Subject: Design and Analysis of Algorithms  
Instructor: Krar Haider  

## Files Included
- dataset.csv → Google stock sample dataset  
- analysis.py → Python code for analysis  
- README.md → Project description import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')
print(data.head())
print(data.describe())

plt.plot(data['Close'])
plt.title("Google Stock Closing Prices")     
plt.show()  

## Description
This project performs basic analysis on Google stock data including:
- Viewing dataset
- Statistical summary
- Visualization of closing prices

## How to Run
1. Install Python
2. Install libraries:
   pip install pandas matplotlib
3. Run:
   python analysis.py
