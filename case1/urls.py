from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^', views.test, name='test_case'),
    url(r'^range/', views.post, name='test'),
    url(r'^admin/', admin.site.urls),

]
