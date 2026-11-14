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
