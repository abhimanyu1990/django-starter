from rest_framework import viewsets
from rest_framework import permissions
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.exceptions import PermissionDenied
from user.permission import IsAdminUser, IsAdminOrAnonymousUser


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ToDoViewSet(viewsets.ModelViewSet):
   
    permission_classes = (IsAuthor,IsAdminOrAnonymousUser)
    serializer_class = ToDoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            
            return ToDo.objects.all()
        if user.is_authenticated:
            return ToDo.objects.filter(author=user)
        raise PermissionDenied()

    def perform_create(self,serializer):
        
        if self.request.user.is_superuser == "admin":
           serializer.save(author=self.request.author)
        elif self.request.user :
            serializer.save(author=self.request.user)