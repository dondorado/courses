from django.conf.urls import url

from .views import (UpdateModelDetailAPIView,
					UpdateModelListAPIView
					)

urlpatterns = [
	url(r'^$', UpdateModelListAPIView.as_view()), # api/updates adresa jer je to osnovna definisana u nemanjaapi.urls 
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
    ]
 