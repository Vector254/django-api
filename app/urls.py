from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/projects/project-id/(\d+)',views.ProjectDescription.as_view())

    
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

