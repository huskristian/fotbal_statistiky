from django.urls import include, path
from rest_framework import routers
from fotbal_liga import views

router = routers.DefaultRouter()
router.register(r'tymy', views.TymViewSet)
router.register(r'hraci', views.HracViewSet)
router.register(r'zapasy', views.ZapasViewSet)
router.register(r'statistiky', views.StatistikyZapasuViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
