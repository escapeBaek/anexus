from django.shortcuts import render
from coag.models import Coag

# Create your views here.
def coag_index(request):
    coags = Coag.objects.all()
    context = {
        'coags': coags,
    }
    return render(request, 'coag/coag_index.html', context)

def coag_detail(request, drugName):
    coag = Coag.objects.get(drugName=drugName)
    context = {
        'coag': coag,
    }
    return render(request, 'coag/coag_detail.html', context)
