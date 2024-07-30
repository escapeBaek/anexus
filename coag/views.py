from django.shortcuts import render
from coag.models import Coag
from accounts.decorators import user_is_approved


@user_is_approved
def coag_landing_page(request):
    return render(request, 'coag/landing_page.html')

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
