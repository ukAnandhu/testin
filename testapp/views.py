from django.shortcuts import render

# Create your views here.
def test(req):
    return render(req,'base.html')