from django.contrib.auth.models import User, Group
from rest_framework import serializers
import models 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MTRRelationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRRelations
        fields = ('relation_id', 'mtr' , 'heat_number')


class MTRChemistrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRChemistry
        fields = ('relation_id', 'sample', 'c', 'mn', 'p', 'chemistry_notes')

class MTRHeatTreatmentProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRHeatTreatmentProcess
        fields = ('relation_id', 'batch', 'pieces', 'process', 'time_units', 'time', 'temperature_unit', 'range', 'temperature', 'cooling_method', 'process_notes')

class MTRMaterialTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRMaterialType
        fields = ('material_type_id', 'material_type')

class MTRSubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRSub
        fields = ('relation_id', 'material_type', 'shape', 'dimensions_unit', 'outside_diameter', 'inside_diameter', 'wall_thickness', 'int_quality', 'condition', 'reduction_type', 'reduction_ratio', 'material_notes')

class MTRHeatTreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRHeatTreatment
        fields = ('relation_id', 'mill_performed', 'heat_treat_vendor', 'lot_number', 'total_pieces', 'heat_treatment_notes')

class MTRSpecificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRSpecifications
        fields = ('specification_id', 'specification_name')

class MTRCustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRCustomers
        fields = ('customer_id', 'customer_name')

class MTRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRS
        fields = ('mtr', 'mill', 'available_inventory', 'customer', 'mtr_attachment', 'customer_specification', 'mtr_notes', 'specifications')

class MTRMaterialTestingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRMaterialTesting
        fields = ('relation_id', 'test_id', 'batch', 'sample', 'vendor_performed', 'lab_vendor', 'mechanical_properties', 'mech_prop_active_results', 'prolongation_surface_hardness', 'prolongation_surface_hardness_active_results', 'quadrant_hardness', 'quadrant_active_results', 'charpy_impacts', 'charpy_impacts_active_results', 'grain_size', 'ndt', 'testing_notes')

class MTRHardnessSubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRHardnessSub
        fields = ('test_id', 'range', 'quadrant', 'OD1', 'OD2', 'OD3', 'OD_Avg', 'MW_1', 'MW_2', 'MW_3', 'MW_Avg', 'ID1', 'ID2', 'ID3', 'ID_Avg')

class MTRSurfaceHardnessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRSurfaceHardness
        fields = ('test_id', 'prolongation_surface', 'quadrant', 'location', 'test_units')

class MTRCharpyImpactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRCharpyImpacts
        fields = ('test_id', 'location', 'direction', 'temperature_unit', 'temperature', 'impact_unit', 'impact1', 'impact2',  'impact3',  'LAT_EXP_unit', 'LAT_EXP1', 'LAT_EXP2', 'LAT_EXP3', 'Shear_D_F1', 'Shear_D_F2', 'Shear_D_F3')


class MTRGrainSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRGrainSize
        fields = ('test_id', 'result1', 'result2')

class MTRNonDestructiveTestingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRNonDestructiveTesting
        fields = ('test_id', 'astm_a388')

class MTRMechanicalPropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MTRMechanicalProperties
        fields = ('test_id', 'tensile_yield_unit', 'tensile', 'yield_2_off', 'yield_6_eul', 'elong_in_2_percent', 'reduction_in_area', 'yield_strength_ratio', 'mechanical_properties_notes')

