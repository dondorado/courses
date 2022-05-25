from django.conf.urls import url, include # include se koristi kad vuce url iz nekog drugog fajla

from .views import (
                    StatusAPIView,
                    StatusAPIDetailView, 
                    #StatusDetailAPIView,
                    
                    )

urlpatterns = [   


    url(r'^$', StatusAPIView.as_view()), 
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),


]


# /api/status/ --> List - svi napravljeni objekti
# /api/status/create/ --> Create - kreiranje objekta
# /api/status/4/ --> Detail (4 je opciono, neki id objekta koji god se izabere)
# /api/status/4/update/ --> Update nekog pojedinacnog objekta
# /api/status/4/delete/ --> Delete nekog pojedinacnog objekta