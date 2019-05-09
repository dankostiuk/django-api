from django.http import HttpResponse
from django.shortcuts import render
from .models import Main

# Create your views here.


def index(request):
    # return HttpResponse('<h3>HELLO FROM MAIN</h3>')

    mains = Main.objects.all()[:10]

    return render(request, 'main/index.html', {
        'title': 'Main',
        'mains': mains
    })


def details(request, id):
    main = Main.objects.get(id=id)

    context = {
        'main': main
    }
    return render(request, 'main/details.html', context)
