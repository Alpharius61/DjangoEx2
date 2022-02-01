from django.contrib import admin
from django.urls import path
from people import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.peopleView),
    path('people/<int:id>', views.peopleDetail)


]
