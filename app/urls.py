from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.q_list, name='q_list'),
    url(r'^result', views.result, name='result'),
]
