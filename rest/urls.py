from django.conf.urls import url, include
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)
router.register(r'owner', views.OwnerViewSet)
router.register(r'pet', views.PetViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
