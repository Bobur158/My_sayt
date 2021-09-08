from django.shortcuts import render
from .models import *

def home(request):
    html = Html.objects.all()
    jquery = Jquery.objects.all()
    bootstrap = Bootstrap.objects.all()
    css = Css.objects.all()
    python = Python.objects.all()
    c = C.objects.all()
    mysql = Mysql.objects.all()
    js = JavaScript.objects.all()
    eng = English.objects.all()
    uz = Uzbek.objects.all()
    tj = Tadjik.objects.all()
    rus = Russian.objects.all()
    tk = Turkish.objects.all()
    title = Title.objects.all() 
    context = {'html': html,'jquery':jquery,'bootstrap':bootstrap,'css':css,'python':python,'c':c,'mysql':mysql,'js':js,'eng':eng,'uz':uz,'tj':tj,'rus':rus,'tk':tk,'title':title}
    return render(request, 'index.html',context)
