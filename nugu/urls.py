from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Nugu API'
API_DESCRIPTION = 'A Web API for calculating and supporting diet.'

urlpatterns = [
    url(r'^', include('nugu_data.urls')),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
