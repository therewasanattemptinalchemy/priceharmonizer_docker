from django.contrib import admin
from django.urls import path, include
import products.urls as products_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(products_urls)),
]
