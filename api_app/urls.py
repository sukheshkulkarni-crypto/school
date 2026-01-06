from rest_framework.routers import DefaultRouter
from .views import StaffViewSet
router=DefaultRouter()
router.register('staffs',StaffViewSet)
urlpatterns=router.urls