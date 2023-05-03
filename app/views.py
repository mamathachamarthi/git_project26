from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        pw=request.POST['pw']
        print(name)
        print(pw)
        return HttpResponse('data will be submitted successfully')
    return render(request,'hai.html')