from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ToDoViewSet

router = SimpleRouter()
router.register('todo', ToDoViewSet, basename="notes")
urlpatterns = router.urls