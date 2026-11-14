# Ex.03 Design a Website for Server Side Processing
## Date: 14-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
index.html

<html>
  <head>
    <title>CALCULATIONS</title>
  </head>
  <body>
    <center>
      <h1>AAKASH M (26001770)</h1>
      <h1>Cumulative Churn Rate</h1>
      <form method="POST">
        {% csrf_token %}
        <label>
          Initial Customers Count :
          <input
            type="number"
            value="{{ Initial_Customers_Count }}"
            name="InitCust"
          />
        </label>
        <br />
        <br />
        <label>
          Customers Lost Count :
          <input
            type="number"
            value="{{ Customers_Lost_Count }}"
            name="CustLost"
          />
        </label>
        <br />
        <br />
        <input type="submit" value="Calculate" />
        <br />
        <br />
        <label>
          Cumulative Churn Rate :
          <input type="number" value="{{ area }}" readonly />
        </label>
      </form>
    </center>
  </body>
</html>

views.py

from django.shortcuts import render

def cumChurn_Rate_area(request):
    Initial_Customers_Count= float(request.POST.get('InitCust', '0'))
    Customers_Lost_Count= float(request.POST.get('CustLost', '0'))

    area = (Customers_Lost_Count / Initial_Customers_Count)*100 if request.method == 'POST' and Initial_Customers_Count != 0 else 0

    print("Initial Customers Count =", Initial_Customers_Count)
    print("Customers Lost Count =", Customers_Lost_Count)
    print("Cumulative Churn Rate =", area)

    return render(
        request,
        'AAKA/index.html',
        {'Initial_Customers_Count': Initial_Customers_Count, 'Customers_Lost_Count': Customers_Lost_Count, 'area': area}
    )

urls.py

from django.contrib import admin
from django.urls import path
from AAKA import views

urlpatterns = [
    path('', views.cumChurn_Rate_area, name='cumChurn_Rate_area'),
]
```

## OUTPUT - SERVER SIDE:

![alt text](<Screenshot (18).png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot (19).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
