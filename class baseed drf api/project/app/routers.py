from rest_framework import routers
from .views import Studentviewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', Studentviewset)

