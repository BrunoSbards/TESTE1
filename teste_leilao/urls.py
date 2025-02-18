from django.contrib import admin
from django.urls import path
from app_leilao import views

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #cadastro
    path('',views.home, name='home'),
    #listagem leiloeiro
    path('leiloeiros/',views.leiloeiros,name='listagem_cadastro'),

]
