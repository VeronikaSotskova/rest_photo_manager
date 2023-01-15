from rest_framework.routers import SimpleRouter

from src.apps.api.v1 import PhotoViewSet, PhotoUserViewSet

app_name = 'api'

router = SimpleRouter()
router.register('photos', PhotoViewSet, basename='photos')
router.register('photo_users', PhotoUserViewSet, basename='photo_users')

urlpatterns = router.urls
