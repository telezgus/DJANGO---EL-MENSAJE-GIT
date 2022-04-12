"""elMensaje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portada import views as portada_views
from muestra import views as muestra_views
from obras import views as obras_views
from subasta import views as subasta_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portada_views.index, name="index"),
    path('muestras/', muestra_views.muestra, name="muestras"),
    path('obras/', obras_views.obras, name="obras"),
    path('subasta/', subasta_views.subasta, name="subasta"),
    path('contacto/',  core_views.contacto, name="contacto"),
    path('compra/',  core_views.compra, name="compra"),
    path('terms/',  core_views.terms, name="terms"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    