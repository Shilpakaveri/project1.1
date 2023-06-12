from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=pink><h1><center>welcome to shilpait</center></h1></body></html>""")
    return res
