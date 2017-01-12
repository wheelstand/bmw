from django.conf.urls import url, include
from rest_framework import routers
from wheelstand.api import views

router = routers.DefaultRouter()
router.register(r'model', views.ModelsViewSet)
router.register(r'trim', views.TrimViewSet)
router.register(r'modelsshown', views.ModelsShownViewSet)
router.register(r'featuresaccessory', views.FeaturesAccessoryViewSet)
#router.register(r'exterior', views.ExteriorViewSet)
router.register(r'upholstery', views.UpholsteryViewSet)
router.register(r'wheel', views.WheelViewSet)
router.register(r'package', views.PackageViewSet)
#router.register(r'option', views.OptionViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'interior', views.InteriorViewSet)
#router.register(r'performance', views.PerformanceViewSet)
router.register(r'colour', views.ColoursViewSet)
#router.register(r'allapi', views.AllAPIView)
#router.register(r'information', views.InformationViewSet)
#router.register(r'testdrive', views.TestDriveViewSet)
#router.register(r'keepingintouch', views.KeepingInTouchList)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^information/$', views.InformationList.as_view()),
    url(r'^testdrive/$', views.TestDriveList.as_view()),  
    url(r'^keepingintouch/$', views.KeepingInTouchList.as_view()),        
    url('^allapi/$', views.AllAPIView.as_view()),
    url('^allapiimages/$', views.AllAPIImagesView.as_view()),    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]