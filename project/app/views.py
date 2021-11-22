from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def chun(request):
    with open('/home/ijin22/test/project/static/chun.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)

    attractiondict = []
    for attraction in attractions:
        content = {
            "title": attraction['판매처명'],
            "x": str(attraction['위도']),
            "y": str(attraction['경도']),
        }
        attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'chun.html', {'attractionJson': attractionJson})

def mil(request):
    with open('/home/ijin22/test/project/static/mil.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)

    attractiondict = []
    for attraction in attractions:
        content = {
            "title": attraction['판매처명'],
            "x": str(attraction['위도']),
            "y": str(attraction['경도']),
        }
        attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'mil.html', {'attractionJson': attractionJson})

def gaw(request):
    with open('/home/ijin22/test/project/static/gaw.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)

    attractiondict = []
    for attraction in attractions:
        content = {
            "title": attraction['판매처명'],
            "x": str(attraction['위도']),
            "y": str(attraction['경도']),
        }
        attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'gaw.html', {'attractionJson': attractionJson})
    
def gyeong(request):
    with open('/home/ijin22/test/project/static/gg.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)

    attractiondict = []
    for attraction in attractions:
        content = {
            "local": attraction['시군명'],
            "title": attraction['사업장명'],
            "x": str(attraction['위도']),
            "y": str(attraction['경도']),
        }
        attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'gg.html', {'attractionJson': attractionJson})