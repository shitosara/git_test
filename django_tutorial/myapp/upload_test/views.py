from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from .models import FileName
import sys, os

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


# Create your views here.
def form(request):
    if request.method == 'GET':
        return render(request, 'upload_test/form.html')

    file = request.FILES['file']
    path = os.path.join(UPLOAD_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    insert_data = FileName(file_name = file.name)
    insert_data.save()

    return redirect("complete")


def complete(request):
    return render(request, 'upload_test/complete.html')
