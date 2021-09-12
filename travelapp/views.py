from django.http import HttpResponse
from django.shortcuts import render
from . models import place
def fun(request):
    obj=place.objects.all()

    return render(request,"index.html",{'results':obj})

def add_product(request):
    if request.method=="POST":
        name=request.POST.get("name")
        img = request.FILES["img"]
        des = request.POST.get("des")
        price = request.POST.get("price")

        s=place(name=name,img=img,des=des,price=price)
        s.save()
    return render(request,"add_product.html")
def add(request):
    num1=int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    num3 = num1+num2
    return render(request,"result.html",{"add":num3})
