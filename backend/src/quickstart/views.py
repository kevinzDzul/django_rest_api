from django.contrib.auth.models import User, Group
from rest_framework import (generics,viewsets)
import models
import serializers




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


#List , Retrieve , Create
class MTRRelationsListViewSet(generics.ListAPIView):
    queryset = models.MTRRelations.objects.all()
    serializer_class = serializers.MTRRelationsSerializer

class MTRRelationsDetailViewSet(generics.RetrieveAPIView):
    queryset = models.MTRRelations.objects.all()
    serializer_class = serializers.MTRRelationsSerializer


class MTRRelationsCreateViewSet(generics.CreateAPIView):
    queryset = models.MTRRelations.objects.all()
    serializer_class = serializers.MTRRelationsSerializer
#end


class MTRRelationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MTRRelations to be viewed or edited.
    """
    queryset = models.MTRRelations.objects.all()
    serializer_class = serializers.MTRRelationsSerializer




class MTRChemistryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MTRRelations to be viewed or edited.
    """
    queryset = models.MTRChemistry.objects.all()
    serializer_class = serializers.MTRChemistrySerializer

class MTRHeatTreatmentProcessViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRHeatTreatmentProcess.objects.all()
    serializer_class = serializers.MTRHeatTreatmentProcessSerializer

class MTRMaterialTypeViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRMaterialType.objects.all()
    serializer_class = serializers.MTRMaterialTypeSerializer

class MTRSubViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRSub.objects.all()
    serializer_class = serializers.MTRSubSerializer

class MTRHeatTreatmentViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRHeatTreatment.objects.all()
    serializer_class = serializers.MTRHeatTreatmentSerializer

class MTRSpecificationsViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRSpecifications.objects.all()
    serializer_class = serializers.MTRSpecificationsSerializer

class MTRCustomersViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRCustomers.objects.all()
    serializer_class = serializers.MTRCustomersSerializer

class MTRSViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRS.objects.all()
    serializer_class = serializers.MTRSerializer

class MTRMaterialTestingViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRMaterialTesting.objects.all()
    serializer_class = serializers.MTRMaterialTestingSerializer


class MTRHardnessSubViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRHardnessSub.objects.all()
    serializer_class = serializers.MTRHardnessSubSerializer


class MTRSurfaceHardnessViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRSurfaceHardness.objects.all()
    serializer_class = serializers.MTRSurfaceHardnessSerializer


class MTRCharpyImpactsViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRCharpyImpacts.objects.all()
    serializer_class = serializers.MTRCharpyImpactsSerializer

class MTRGrainSizeViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRGrainSize.objects.all()
    serializer_class = serializers.MTRGrainSizeSerializer

class MTRNonDestructiveTestingViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRNonDestructiveTesting.objects.all()
    serializer_class = serializers.MTRNonDestructiveTestingSerializer


class MTRMechanicalPropertiesViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = models.MTRMechanicalProperties.objects.all()
    serializer_class = serializers.MTRMechanicalPropertiesSerializer