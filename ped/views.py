from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import user_is_approved



@user_is_approved
def ped_landing_page(request):
    return render(request, 'ped/landing_page.html')

def pedcalculate(request):
    age = request.GET.get('age')
    height = request.GET.get('height')
    weight = request.GET.get('weight')

    if age and weight and height:
        age = float(age)
        weight = float(weight)
        height = float(height)
        
        ett_id = (age / 4) + 3.5
        ett_depth = (age / 2) + 12
        atropine = weight * 0.02
        tpt = weight * 6
        roc = weight * 0.6
        lidocaine = weight * 0.5
        propofol = weight * 2
        ftn = weight * 1
        ond = weight * 0.1
        dng = weight * 15

        # Calculating ml values
        lidocaine_ml = lidocaine / 10
        propofol_ml = propofol / 10
        atropine_ml = atropine * 2
        tpt_ml = tpt / 25
        roc_ml = roc / 10
        ftn_ml = ftn / 50
        ond_ml = ond / 2
        dng_ml = dng / 200

        # Calculating C line
        if height >= 100:
            c_line = height / 10 - 2
        else:
            c_line = height / 10 - 1.5
    else:
        ett_id = ett_depth = atropine = tpt = roc = lidocaine = propofol = ftn = ond = dng = 'Invalid input'
        lidocaine_ml = propofol_ml = atropine_ml = tpt_ml = roc_ml = ftn_ml = ond_ml = dng_ml = 'Invalid input'
        c_line = 'Invalid input'

    context = {
        'ett_id': ett_id,
        'ett_depth': ett_depth,
        'atropine': atropine,
        'tpt': tpt,
        'roc': roc,
        'lidocaine': lidocaine,
        'propofol': propofol,
        'ftn': ftn,
        'ond': ond,
        'dng': dng,
        'lidocaine_ml': lidocaine_ml,
        'propofol_ml': propofol_ml,
        'atropine_ml': atropine_ml,
        'tpt_ml': tpt_ml,
        'roc_ml': roc_ml,
        'ftn_ml': ftn_ml,
        'ond_ml': ond_ml,
        'dng_ml': dng_ml,
        'c_line': c_line,
        'age': age,
        'height': height,
        'weight': weight
    }
    return render(request, 'ped/pedcalc.html', context)
