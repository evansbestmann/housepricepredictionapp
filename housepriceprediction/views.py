from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# Create your views here.
def home(request):
    return render (request,"home.html")
#####################################################################################################3
def predictwoji(request):
    return render (request,"predictwoji.html")

def resultwoji(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predictwoji.html",{"price":price})
#############################################################################################################
def predictgra(request):
    return render (request,"predictgra.html")

def resultgra(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predictgra.html",{"price":price})
#####################################################################################################3
def predictruk(request):
    return render (request,"predictruk.html")

def resultruk(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predictruk.html",{"price":price})
#############################################################################################################
#####################################################################################################3
def predicttrans(request):
    return render (request,"predicttrans.html")

def resulttrans(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predicttrans.html",{"price":price})
#############################################################################################################
def predictada(request):
    return render (request,"predictada.html")

def resultada(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predictada.html",{"price":price})
#####################################################################################################3
def predictdiobu(request):
    return render (request,"predictdiobu.html")

def resultdiobu(request):
    data = pd.read_csv(r"C:\Users\EliteBook\Desktop\housedata\USA_Housing.csv")
    data = data.drop(["Address"], axis=1)
    x = data.drop(["Price"], axis=1)
    y = data.Price
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.90)
    # TEST SIZE .30 MEANS 30% OF DATA WILL BE THE TEST PART AND 70% FOR TRAINING
    model = LinearRegression()
    model.fit(x_train, y_train)


    Avg_Area_income=float(request.GET['n1'])
    Avg_Area_House_Age=float(request.GET['n2'])
    Avg_Area_Room_No=float(request.GET['n3'])
    Avg_Bedroom_No=float(request.GET['n4'])
    Avg_Area_Population=float(request.GET['n5'])

    pred=model.predict(np.array([Avg_Area_income,Avg_Area_House_Age,Avg_Area_Room_No,Avg_Bedroom_No,Avg_Area_Population]).reshape(1,-1))
    pred=float(pred[0])


    price="The predicted price is $"+ str (pred)
    return render (request,"predictdiobu.html",{"price":price})
############################################################################################################