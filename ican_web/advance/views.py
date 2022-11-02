from django.shortcuts import render

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