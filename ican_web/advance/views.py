from django.shortcuts import render

def landing(request):

    return render(
        request,
        'advance/base.html',
    )

def login(request):

    return render(
        request,
        'advance/login.html',
    )

def mypage(request):
    return render(
        request,
        'advance/mypage.html',
    )

