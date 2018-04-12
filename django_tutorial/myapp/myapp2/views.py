from django.shortcuts import render
from django.http import HttpResponse
from .models import Songs

# Create your views here.
def index(request):
    # 文字列返す
    # return HttpResponse("HelloWorld!!")
    # return render(request, 'songs/index.html')
    songs = Songs.objects.all().order_by('id')  # 値を取得
    return render(request, 'songs/index.html', {'songs': songs})  # Templateに値を渡す

def songs(request):
    # 文字列返す
    return HttpResponse("ListenMySongs!!")