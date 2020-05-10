from django.conf.urls import url
from pttrack.urls import wrap_url
from django.views.generic import DetailView

from . import models
from . import views

unwrapped_urlpatterns = [
    url(r'^$',
        views.drug_list,
        name="drug-list"),
]

wrap_config = {}
urlpatterns = [wrap_url(u, **wrap_config) for u in unwrapped_urlpatterns]
