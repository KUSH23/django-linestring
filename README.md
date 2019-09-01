# django-linestring

pip install django

pip install GDAL


# if found error related to GDAL
check your GDAL version in {Python root}\Lib\site-packages\osgeo in my case C:\Python37\Lib\site-packages\osgeo
and add your version of gdal in line 26 in C:\Python37\Lib\site-packages\django\contrib\gis\gdal/libgdal.py

# run Locally
open cmd at your django project and run "python manage.py runserver"
open http://127.0.0.1:8000/ in browser
