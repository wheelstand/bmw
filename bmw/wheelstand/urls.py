from django.conf.urls import url
from .views import TrimList, TrimDetail
from .models import Trim

urlpatterns = [
    url(r'^$', TrimList.as_view(), name='listing'),
 	url(r'^(?P<slug>[\w-]+)/$', TrimDetail.as_view(), name='trim_view'),    
]