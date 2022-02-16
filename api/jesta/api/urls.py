from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'elders', views.ElderViewSet)
router.register(r'sons', views.SonViewSet)
router.register(r'professions', views.ProfessionViewSet)
router.register(r'pro', views.ProViewSet)
router.register(r'call', views.CallViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]