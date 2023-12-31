from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.doctors, name='contact'),
    path('add/', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),

    path('upload/', views.upload_image, name='upload'),
    path('image/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
]
