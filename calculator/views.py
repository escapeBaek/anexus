from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    
    #Input area
    age = request.GET.get('age')
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    
    nep_conc = request.GET.get('nep_conc')
    nep_dr = request.GET.get('nep_dr')
    
    epi_conc = request.GET.get('epi_conc')
    epi_dr = request.GET.get('epi_dr')
    
    dopa_conc = request.GET.get('dopa_conc')
    dopa_dr = request.GET.get('dopa_dr')
    
    dobu_conc = request.GET.get('dobu_conc')
    dobu_dr = request.GET.get('dobu_dr')
    
    ntg_conc = request.GET.get('ntg_conc')
    ntg_dr = request.GET.get('ntg_dr')
    
    snp_conc = request.GET.get('snp_conc')
    snp_dr = request.GET.get('snp_dr')
    
    vaso_conc = request.GET.get('vaso_conc')
    vaso_dr1 = request.GET.get('vaso_dr1')
    vaso_dr2 = request.GET.get('vaso_dr2')
    
    ppf_conc = request.GET.get('ppf_conc')
    
    rftn_conc = request.GET.get('rftn_conc')
    
    suftn_conc = request.GET.get('suftn_conc')
    
    txa_conc = request.GET.get('txa_conc')
    
    
    #Output area
    nep_result = 0
    epi_result = 0
    dopa_result = 0
    dobu_result = 0
    ntg_result = 0
    snp_result = 0
    vaso_result1 = 0
    vaso_result2 = 0
    ppf_result1 = 0
    ppf_result2 = 0
    rftn_result1 = 0
    rftn_result2 = 0
    suftn_result1 = 0
    suftn_result2 = 0
    txa_result1 = 0
    txa_result2 = 0
    
    
    ##Calculation area
    #NEP Calculation
    if weight and nep_conc and nep_dr:
        weight = int(weight)
        nep_conc = float(nep_conc)
        nep_dr = float(nep_dr)
        nep_result = 60*weight*nep_dr/nep_conc
    else:
        nep_result = "!!Please fill all the fields!!"
        
    #EPI Calculation
    if weight and epi_conc and epi_dr:
        weight = int(weight)
        epi_conc = float(epi_conc)
        epi_dr = float(epi_dr)
        epi_result = 60*weight*epi_dr/epi_conc
    else:
        epi_result = "!!Please fill all the fields!!"
        
    #Dopa Calculation
    if weight and dopa_conc and dopa_dr:
        weight = int(weight)
        dopa_conc = float(dopa_conc)
        dopa_dr = float(dopa_dr)
        dopa_result = (60*weight*dopa_dr)/(dopa_conc*1000)
    else:
        dopa_result = "!!Please fill all the fields!!"
        
    #Dobu Calculation
    if weight and dobu_conc and dobu_dr:
        weight = int(weight)
        dobu_conc = float(dobu_conc)
        dobu_dr = float(dobu_dr)
        dobu_result = (60*weight*dobu_dr)/(dobu_conc*1000)
    else:
        dobu_result = "!!Please fill all the fields!!"
        
    #Ntg Calculation
    if weight and ntg_conc and ntg_dr:
        weight = int(weight)
        ntg_conc = float(ntg_conc)
        ntg_dr = float(ntg_dr)
        ntg_result = (60*weight*ntg_dr)/(ntg_conc*1000)
    else:
        ntg_result = "!!Please fill all the fields!!"
        
    #Snp Calculation
    if weight and snp_conc and snp_dr:
        weight = int(weight)
        snp_conc = float(snp_conc)
        snp_dr = float(snp_dr)
        snp_result = (60*weight*snp_dr)/(snp_conc*1000)
    else:
        snp_result = "!!Please fill all the fields!!"
    
    #Vaso Calculation
    if weight and vaso_conc and vaso_dr1 and vaso_dr2:
        vaso_conc = float(vaso_conc)
        vaso_dr1 = float(vaso_dr1)
        vaso_dr2 = float(vaso_dr2)
        vaso_result1 = (60*vaso_dr1)/(vaso_conc)
        vaso_result2 = (weight*vaso_dr2)/(vaso_conc)
    else:
        vaso_result1 = "!!Please fill all the fields!!"
        vaso_result2 = "!!Please fill all the fields!!"
        
    #PPF Calculation
    if weight and ppf_conc:
        ppf_conc = float(ppf_conc)
        ppf_result1 = (weight*6)/ppf_conc
        ppf_result2 = (weight*12)/ppf_conc
    else:
        ppf_result1 = "!!Please fill all the fields!!"
        ppf_result2 = "!!Please fill all the fields!!"
        
    #RFTN Calculation
    if weight and rftn_conc:
        rftn_conc = float(rftn_conc)
        rftn_result1 = (weight*0.1)/rftn_conc
        rftn_result2 = (weight*1)/rftn_conc
    else:
        rftn_result1 = "!!Please fill all the fields!!"
        rftn_result2 = "!!Please fill all the fields!!"
        
    #SUFTN Calculation
    if weight and suftn_conc:
        suftn_conc = float(suftn_conc)
        suftn_result1 = (weight*0.5)/suftn_conc
        suftn_result2 = (weight*1.5)/suftn_conc
        
    #TXA Calculation
    if weight and txa_conc:
        txa_conc = float(txa_conc)
        txa_result1 = (weight*10*3)/(txa_conc)
        txa_result2 = (weight*1)/(txa_conc)
    else:
        txa_result1 = "!!Please fill all the fields!!"
        txa_result2 = "!!Please fill all the fields!!"
        
    return render(request, 'calculator/calculator.html', {'nep_result':nep_result, 'epi_result':epi_result, 'dopa_result':dopa_result, 'dobu_result':dobu_result, 'ntg_result':ntg_result, 'snp_result':snp_result, 'vaso_result1':vaso_result1, 'vaso_result2':vaso_result2, 'ppf_result1':ppf_result1, 'ppf_result2':ppf_result2, 'rftn_result1':rftn_result1, 'rftn_result2':rftn_result2, 'suftn_result1':suftn_result1, 'suftn_result2':suftn_result2, 'txa_result1':txa_result1, 'txa_result2':txa_result2})