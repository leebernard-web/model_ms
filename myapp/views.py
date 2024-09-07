from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from joblib import load

model = load('./savedModels/model.joblib')

def home(request):

    if request.method == 'post':
        sepal_length = request.post["sepal_length"]
        sepal_width = request.post["sepal_width"]
        petal_length = request.post["petal_length"]
        petal_width = request.post["petal_width"]

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if y_pred [0]== 0:
            y_pred = "Setosa"
        elif y_pred[0] == 1:
            y_pred = "Vercicolor"
        else:
            y_pred = "Virginica"

        return render(request, 'myapp/home.html' , {'result' : y_pred})
        


        print(y_pred)

    return render(request, "myapp/home.html")