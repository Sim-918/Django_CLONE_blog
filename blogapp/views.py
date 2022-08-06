from django.shortcuts import render

# Create your views here.
def index(request):
    context={

    }
    return render(request,"index.html",context=context)

def single(request):
    context={

    }
    return render(request,"single.html",context=context)