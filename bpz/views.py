from rest_framework import viewsets

from .models import Case, HomeOwnersAssociation
from .serializers import CaseSerializer, HomeOwnersAssociationSerializer


class CaseViewSet(viewsets.ModelViewSet):
    model = Case
    serializer_class = CaseSerializer


class HOAViewSet(viewsets.ModelViewSet):
    model = HomeOwnersAssociation
    serializer_class = HomeOwnersAssociationSerializer
