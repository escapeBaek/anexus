from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

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
        {'name': 'Oxytoxin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0210A0250'},
        {'name': 'ATG', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AMMMMM1692'},
        {'name': 'Basiliximab', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ACCCCC0369'},
        {'name': 'Insulin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AEEEEE0625'},
        {'name': 'Potassium', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB2765'},
        {'name': 'NO', 'url': 'https://www.rxlist.com/nitric_oxide_gas/generic-drug.htm'},
        {'name': 'N2O', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08G1299'},
        {'name': 'Sevoflurane', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11APPPPP1736'},
        {'name': 'Desflurane', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11ABBBBB1318'},
        {'name': 'Enflurane', 'url': 'https://www.rxlist.com/ethrane-drug.htm'},
        {'name': 'Isoflurane', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08C0009'},
        {'name': 'Halothane', 'url': 'https://www.rxlist.com/fluothane-drug.htm'},
        {'name': 'Carbetocin', 'url': 'https://health.kr/searchDrug/result_drug.asp?drug_cd=2017071700001'},
        {'name': 'Haloperidol', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0920A0104'},
        {'name': 'PDRN', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2021011300011'},
        {'name': 'Methylergonovine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AMMMMM2973'},
        {'name': 'Metoclopramide', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0490B0002'},
        {'name': 'Cimetidine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AOOOOO9280'},
        {'name': 'Hepatitis B Immunoglobulin', 'url': 'https://www.health.kr/searchDrug/result_take.asp?drug_cd=A11APPPPP1479'},
        {'name': 'Dexmedetomidine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2010060700005'},
        {'name': 'Cefazolin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AKP08G1108'},
        {'name': 'Ceftriaxone', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A0101A0351'},
        {'name': 'Vancomycin', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AOOOOO1540'},
        {'name': 'Metronidazole', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11AMMMMM1000'},
        {'name': 'Adenosine', 'url': 'https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2013080600009'},
        
        # 추가할 다른 약들
    ]
    
    # Sort the list of dictionaries by the 'name' key
    sorted_drugs = sorted(drugs, key=lambda x: x['name'])

    return render(request, 'drugdictionary/drug_list.html', {'drugs': drugs, 'sorted_drugs': sorted_drugs})

def search_drug(request):
    query = request.GET.get('q', '').strip()  # Get the search query
    print(f"🔍 Search Query: {query}")  # Debugging

    if not query:
        return render(request, 'drugdictionary/drug_list.html', {'sorted_drugs': []})

    # ✅ Corrected Search URL
    search_url = f"https://www.health.kr/searchDrug/search_total_result.asp?search_value={query}"
    print(f"🔗 Requesting: {search_url}")  # Debugging

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Request Failed: {response.status_code}")
        return render(request, 'drugdictionary/drug_list.html', {'sorted_drugs': []})

    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"✅ Page Fetched Successfully")  # Debugging

    # ✅ New Selector Based on Actual HTML Structure
    drug_list = []
    table_rows = soup.select('table tr')[1:]  # Skip the first row (header)

    for row in table_rows:
        columns = row.select('td')

        if len(columns) < 3:
            continue  # Skip rows without enough columns

        name = columns[1].text.strip()  # Product name
        component = columns[2].text.strip()  # Active ingredient
        company = columns[5].text.strip()  # Manufacturer

        # Extract the link (Modify this if structure changes)
        link_tag = columns[1].select_one('a')
        url = f"https://www.health.kr/{link_tag['href']}" if link_tag else '#'

        drug_list.append({
            'name': name,
            'subtitle': f"{component} - {company}",
            'url': url
        })

    print(f"📌 Extracted {len(drug_list)} drugs")  # Debugging

    return render(request, 'drugdictionary/drug_list.html', {'sorted_drugs': drug_list})