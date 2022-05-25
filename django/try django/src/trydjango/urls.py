"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import (home_page,
about_page,
contact_page,
example_page)
from blog.views import blog_post_create_view
from searches.views import search_view

urlpatterns = [
	path('', home_page),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    #path('blog/<int:id>', blog_post_detail_page), id je ono sto na view (blog_post_detail_page) ima sem request kao parametar

    path('search/', search_view),
    path('blog-new/', blog_post_create_view),
    path('about/', about_page),
    path('contact/', contact_page),
    path('example/', example_page),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #ovo se radi kako bi slika koju ubacimo mogla da se vidi. Pre sve mora da se importuje settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
