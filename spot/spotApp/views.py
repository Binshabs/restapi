from django.shortcuts import render
import requests

# Create your views here.

def Home(request):
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
   
    return render(request,'index.html',{'datas':data})
