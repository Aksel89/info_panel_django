from django.shortcuts import render


def Index(request):
    return render(request, 'info_panel/index.html')


def atlas_professiy(request):
    return render(request, 'info_panel/atlas_professiy.html')


def den_rojdenya(request):
    return render(request, 'info_panel/den_rojdenya.html')


def dostoprim(request):
    return render(request, 'info_panel/dostoprim.html')


def exscursion(request):
    return render(request, 'info_panel/exscursion.html')


def index_eng(request):
    return render(request, 'info_panel/index_eng.html')


def jivie_uroki(request):
    return render(request, 'info_panel/jivie_uroki.html')


def kak_eto_sdelano(request):
    return render(request, 'info_panel/kak_eto_sdelanno.html')


def kvesti(request):
    return render(request, 'info_panel/kvesti.html')


def lessons(request):
    return render(request, 'info_panel/lessons.html')


def mappesh(request):
    return render(request, 'info_panel/mappesh.html')


def mappesh_eng(request):
    return render(request, 'info_panel/mappesh_eng.html')


def metro(request):
    return render(request, 'info_panel/metro.html')


def metro_eng(request):
    return render(request, 'info_panel/metro_eng.html')


def partners(request):
    return render(request, 'info_panel/partners.html')


def quiz(request):
    return render(request, 'info_panel/quiz.html')


def sale(request):
    return render(request, 'info_panel/sale.html')


def taxi(request):
    return render(request, 'info_panel/taxi.html')


def taxi_eng(request):
    return render(request, 'info_panel/taxi_eng.html')
