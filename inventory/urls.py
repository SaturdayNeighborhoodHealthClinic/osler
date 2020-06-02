from django.conf.urls import url
from pttrack.urls import wrap_url
from django.views.generic import DetailView

from . import models
from . import views

unwrapped_urlpatterns = [
    url(r'^$', views.drug_list, name="drug-list"),
    url(r'^add-drug/$', views.DrugAdd.as_view(), name='drug-add'),
    url(r'^drug/update/(?P<pk>[0-9]+)$',
        views.DrugUpdate.as_view(), name='drug-update'),
]

wrap_config = {}
urlpatterns = [wrap_url(u, **wrap_config) for u in unwrapped_urlpatterns]
