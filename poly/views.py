from django.contrib.gis.geos import LinearRing, Point, Polygon, LineString
from django.shortcuts import render, redirect
from django.contrib.gis.geos import GEOSGeometry
from polygen.models import PolyPoints
from .forms import PostForm

def home_page(request):
    form = PostForm()
    points = PolyPoints.objects.all()
    return render(request, "index.html", {'form': form})

def my_view(request):

    if request.method == 'POST':
        # print(request.POST.get('_lat'))

        form = PostForm(request.POST)
        
        print(form['_lat'].value(),form['_long'].value())
        print(form['_lat1'].value(),form['_long1'].value())
        p1 = Point(float(form['_lat'].value()),float(form['_long'].value()))
        p2 = Point(float(form['_lat1'].value()),float(form['_long1'].value()))
        ls = LineString( [p1, p2] )
        qq = ls.length
        
        print(qq)
    data = {
        'qq':qq
    }
    return render(request, "result.html",{'qq':qq})