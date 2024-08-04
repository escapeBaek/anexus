from django.shortcuts import render, reverse

def home(request):
    cards = [
        {"title": "Coagulation Guideline", "text": "Find the latest coagulation guidelines.", "url": reverse('coag_index')},
        {"title": "Drug Calculator", "text": "Accurate drug dosage calculations.", "url": reverse('calculator')},
        {"title": "Pediatric Calculator", "text": "Accurate calculations for pediatric anesthesia.", "url": reverse('pedcalculate')},
        {"title": "Board", "text": "Join discussions and share knowledge.", "url": reverse('board_index')},
        {"title": "Question Bank", "text": "More information about board exam.", "url": reverse('exam_list')},
        {"title": "SNUH Anesthesia", "text": "More information for alumni.", "url": "https://dept.snuh.org/dept/AN/index.do"},
        {"title": "KSA", "text": "Korean Society of Anesthesiologists.", "url": "https://www.anesthesia.or.kr/"},
        {"title": "NYSORA", "text": "World-wide renowned educational organization with focus in anesthesiology.", "url": "https://www.nysora.com/"},
        {"title": "OrphanAnesthesia", "text": "Anesthesia care for rare diseases.", "url": "https://www.orphananesthesia.eu/en/rare-diseases/published-guidelines.html"},
        {"title": "OrphanAnesthesia", "text": "Anesthesia care for rare diseases.", "url": "https://www.orphananesthesia.eu/en/rare-diseases/published-guidelines.html"},
        {"title": "Virtual TEE", "text": "Virtual TEE for education.", "url": "https://pie.med.utoronto.ca/TEE/TEE_content/TEE_standardViews_intro.html"},
        {"title": "Virtual FOB", "text": "Virtual FOB for education.", "url": "https://pie.med.utoronto.ca/VB/VB_content/simulation.html"},
        {"title": "Notion test 1", "text": "Testing for notion link.", "url": "https://escapebaek.notion.site/Brachial-Plexus-Block-1bc4d01a2aa648f09917278463b89ce2?pvs=25"},
        {"title": "Notion test 2", "text": "Testing for notion link.", "url": "https://escapebaek.notion.site/ERAS-PONV-Guideline-92a68b5dbb85474a85eeee278b636bc7?pvs=4"},
    ]
    return render(request, 'land/home.html', {'cards': cards})