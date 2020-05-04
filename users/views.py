from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import Company
from users.serializers import CompanySerializer


class CompanyViewSet(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
