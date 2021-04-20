"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from pages import views
from django.contrib import admin
from django.urls import path
from products.views import product_detail_view, product_create_view, product_delete_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('contacts/', views.contacts_view),
    path('about/', views.about_view),
    path('social/', views.social_view),
    path('create/', product_create_view),
    path('product/', product_detail_view),
    path('product/<int:my_id>/', product_detail_view),
    path('product/<int:my_id>/delete/', product_delete_view, name='product-delete')
]
