from rest_framework.routers import DefaultRouter

from bmi_log.views import BMIViewSet


router = DefaultRouter()
router.register(r'bmi-log', BMIViewSet)

urlpatterns = router.urls
