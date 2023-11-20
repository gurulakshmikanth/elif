from django.shortcuts import render

# Create your views here.
def com(request):
    d={'a':10,'b':2,'c':3}
    return render(request,'com.html',d)