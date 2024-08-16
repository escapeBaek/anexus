# drugdictionary/views.py

from django.shortcuts import render

def drug_list(request):
    drugs = [
        {'name': 'Atropine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0490A0024'},
        {'name': 'Lidocaine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0490A0027'},
        {'name': 'Pyridostigmine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA3953'},
        {'name': 'Neostigmine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB2740'},
        {'name': 'Glycopyrrolate', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A3180A0054'},
        {'name': 'Sugammadex', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2012101600008'},
        {'name': 'Ramosetron', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGG5334'},
        {'name': 'Palonosetron', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2017022100002'},
        {'name': 'Dexamethasone', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0450A0362'},
        {'name': 'Rocuronium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2010062500009'},
        {'name': 'Vecuronium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0140A0149'},
        {'name': 'Norepinephrine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AJJJJJ0075'},
        {'name': 'Propofol(1%)', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2011022800019'},
        {'name': 'Propofol(2%)', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2011022800014'},
        {'name': 'Succinylcholine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08C0017'},
        {'name': 'Fentanyl', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB0167'},
        {'name': 'Sufentanil', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA0632'},
        {'name': 'Remifentanil', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=t4lc5mpbn2qil'},
        {'name': 'Dantrolene', 'url': 'https://www.rxlist.com/dantrolene/generic-drug.htm'},
        {'name': 'Vasopressin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A3780A0069'},
        {'name': 'Dopamine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A3780A0047'},
        {'name': 'Dobutamine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A3180A0326'},
        {'name': 'Phenylephrine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A2040B0030'},
        {'name': 'Ephedrine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A1280A0002'},
        {'name': 'Vitamin K', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB2803'},
        {'name': 'Tranexamic Acid', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0030A0280'},
        {'name': 'Midazolam', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AOOOOO1669'},
        {'name': 'Diazepam', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB0010'},
        {'name': 'Magnesium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AMMMMM0030'},
        {'name': 'Calcium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0270B0067'},
        {'name': 'Lorazepam', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AOOOOO0022'},
        {'name': 'Flumazenil', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2011102400008'},
        {'name': 'Naloxone', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0140A0098'},
        {'name': 'Methylpredisolone', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0720A0502'},
        {'name': 'Remimazolam', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2021010800012'},
        {'name': 'Desmopressin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB2541'},
        {'name': 'Etomidate', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA0323'},
        {'name': 'Ketamine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA0348'},
        {'name': 'Bupivacaine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ACCCCC0537'},
        {'name': 'Ropivacaine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08G1535'},
        {'name': 'Mepivacaine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0140A0114'},
        {'name': 'Diltiazem', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0101A0268'},
        {'name': 'Chlorpheniramine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA4329'},
        {'name': 'Ventolin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB1232'},
        {'name': 'Epinephrine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0490A0034'},
        {'name': 'Nitroglycerin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AGGGGA2469'},
        {'name': 'Nitroprusside', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08G0406'},
        {'name': 'Thiopental', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB2121'},
        {'name': 'Propacetamol', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0690A0608'},
        {'name': 'Heparin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0030A0287'},
        {'name': 'Protamine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A3780A0051'},
        {'name': 'Amiodarone', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB0139'},
        {'name': 'Isoproterenol', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2024041700006'},
        {'name': 'Cisatracurium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP09F0011'},
        {'name': 'Atracurium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A2040A0197'},
        
        
        
        

        
        
        # 추가할 다른 약들
    ]
    
    # Sort the list of dictionaries by the 'name' key
    sorted_drugs = sorted(drugs, key=lambda x: x['name'])

    return render(request, 'drugdictionary/drug_list.html', {'drugs': drugs, 'sorted_drugs': sorted_drugs})
