from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCRO(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'cro'

class IsASM(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'asm'

class CROCreateView(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'cro' and request.method in ['GET','POST']

class ASMUpdateStatus(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'asm'