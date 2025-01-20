from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import user_is_approved



@user_is_approved
def ped_landing_page(request):
    return render(request, 'ped/landing_page.html')

@user_is_approved
def pedcalculate(request):
    age = request.GET.get('age')
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    
    context = {
        'age': age,
        'height': height,
        'weight': weight
    }

    if age and weight and height:
        try:
            age = float(age)
            weight = float(weight)
            height = float(height)
            
            # Calculate values with proper rounding
            context.update({
                'ett_id': round((age / 4) + 3.5, 1),
                'ett_depth': round((age / 2) + 12, 1),
                'c_line': round(height / 10 - (1.5 if height < 100 else 2), 1),
                
                # Medications in mg/mcg
                'atropine': round(weight * 0.02, 2),
                'lidocaine': round(weight * 0.5, 1),
                'propofol': round(weight * 2, 1),
                'tpt': round(weight * 6, 1),
                'roc': round(weight * 0.6, 1),
                'ftn': round(weight * 1, 1),
                'dng': round(weight * 15, 1),
                'ond': round(weight * 0.1, 2),
                
                # Volumes in ml
                'atropine_ml': round(weight * 0.02 * 2, 2),
                'lidocaine_ml': round((weight * 0.5) / 10, 2),
                'propofol_ml': round((weight * 2) / 10, 2),
                'tpt_ml': round((weight * 6) / 25, 2),
                'roc_ml': round((weight * 0.6) / 10, 2),
                'ftn_ml': round((weight * 1) / 50, 2),
                'dng_ml': round((weight * 15) / 200, 2),
                'ond_ml': round((weight * 0.1) / 2, 2)
            })
        except ValueError:
            context.update({
                'error': 'Please enter valid numbers for age, height, and weight.'
            })
    
    return render(request, 'ped/pedcalc.html', context)