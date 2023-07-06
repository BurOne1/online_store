from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about_me.html')


def chat(request):
    return render(request, 'main/test.html')


def flex(request):
    return render(request, 'main/flex.html')
