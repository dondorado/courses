"""nemanjaapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # include se koristi kad vuce url iz nekog drugog fajla
from django.contrib import admin


from updates.views import (
							json_example_view,
							JsonCBV,
							JsonCBV2,
							SerializedDetailView,
							SerializedListView
						  )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/updates/', include('updates.api.urls')), #api/updates/
    url(r'^api/status/', include('status.api.urls', namespace='api-status')), #api/updates/ 
 


    # url(r'^json/cbv/$', JsonCBV.as_view()), # as_viwe built-im za klasu View Djanga
    # url(r'^json/cbv2/$', JsonCBV2.as_view()),
    # url(r'^json/example/$', json_example_view),
    # url(r'^json/serialized/detail/$', SerializedDetailView.as_view()),
    # url(r'^json/serialized/list/$', SerializedListView.as_view()),


]

