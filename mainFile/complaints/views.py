from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Complaint
from .serializers import ComplaintSerializer
from .permissions import IsCRO, IsASM

class ComplaintViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.role == 'cro':
            return Complaint.objects.filter(created_by=user)
        return Complaint.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.request.user.role == 'cro':
            return [IsCRO()]
        return [IsASM()]

    @action(detail=False, methods=['get'])
    def pending_exists(self, request):
        exists = Complaint.objects.filter(feedback_status='pending').exists()
        return Response({'pending': exists})