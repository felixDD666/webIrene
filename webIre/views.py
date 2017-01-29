from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'webIre/index.html',{})

def thanks(request):
    return render(request,'webIre/thanks.html',{})