from django.urls import include, path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path(r'', TemplateView.as_view(template_name='main/index.html'))
]
