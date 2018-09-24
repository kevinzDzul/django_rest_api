# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class MTRRelations(models.Model):
    relation_id = models.AutoField(primary_key=True)
    mtr = models.CharField(max_length=255)
    heat_number =  models.CharField(max_length=255)

    

class MTRChemistry(models.Model):
    relation_id = models.ForeignKey(MTRRelations, on_delete=models.CASCADE)
    sample = models.CharField(max_length=100)
    c = models.FloatField()
    mn = models.FloatField()
    p = models.FloatField()
    chemistry_notes = models.CharField(max_length=255)

    


class MTRHeatTreatmentProcess(models.Model):
    relation_id = models.ForeignKey(MTRRelations, on_delete=models.CASCADE)
    batch = models.CharField(max_length=2)
    pieces = models.SmallIntegerField()
    process = models.CharField(max_length=255)
    time_units = models.CharField(max_length=5)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature_unit = models.CharField(max_length=5)
    range = models.BooleanField()
    temperature = models.SmallIntegerField()
    cooling_method = models.CharField(max_length=255)
    process_notes = models.CharField(max_length=255)

    

class MTRMaterialType(models.Model):
    material_type_id = models.AutoField(primary_key=True)
    material_type = models.CharField(max_length=100)

    


class MTRSub(models.Model):
    relation_id  = models.ForeignKey(MTRRelations, on_delete=models.CASCADE)
    material_type  = models.ForeignKey(MTRMaterialType, on_delete=models.CASCADE)
    shape = models.CharField(max_length=10)
    dimensions_unit = models.CharField(max_length=255)
    outside_diameter = models. FloatField()
    inside_diameter = models. FloatField()
    wall_thickness = models. FloatField()
    int_quality = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    reduction_type = models.CharField(max_length=10)
    reduction_ratio = models.CharField(max_length=50)
    material_notes = models.CharField(max_length=255)




class MTRHeatTreatment(models.Model):
    relation_id = models.ForeignKey(MTRRelations, on_delete=models.CASCADE)
    mill_performed = models.BooleanField()
    heat_treat_vendor = models.CharField(max_length=255) 
    lot_number = models.SmallIntegerField()
    total_pieces = models.SmallIntegerField()
    heat_treatment_notes = models.CharField(max_length=255, default='' )




class MTRSpecifications(models.Model):
    specification_id = models.AutoField(primary_key=True)
    specification_name = models.CharField(max_length=100)

 

class MTRCustomers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)

    

class MTRS(models.Model):
    mtr = models.CharField(max_length=255,primary_key=True)
    mill = models.CharField(max_length=100)
    available_inventory = models.BooleanField()
    customer = models.ForeignKey(MTRCustomers, on_delete=models.CASCADE)
    mtr_attachment = models.CharField(max_length=100)
    customer_specification = models.CharField(max_length=100)
    mtr_notes = models.CharField(max_length=255)
    specifications = models.ForeignKey(MTRSpecifications, on_delete=models.CASCADE)

  
class MTRMaterialTesting(models.Model):
    relation_id = models.ForeignKey(MTRRelations, on_delete=models.CASCADE)
    test_id = models.CharField(max_length=255)
    batch = models.CharField(max_length=5)
    sample = models.CharField(max_length=255)
    vendor_performed = models.BooleanField()
    lab_vendor = models.CharField(max_length=100)
    mechanical_properties = models.BooleanField()
    mech_prop_active_results = models.BooleanField()
    prolongation_surface_hardness = models.BooleanField()
    prolongation_surface_hardness_active_results = models.BooleanField()
    quadrant_hardness = models.BooleanField()
    quadrant_active_results = models.BooleanField()
    charpy_impacts = models.BooleanField()
    charpy_impacts_active_results = models.BooleanField()
    grain_size = models.BooleanField()
    ndt = models.BooleanField()
    testing_notes = models.BooleanField()

    


class MTRHardnessSub(models.Model):
    test_id = models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    range = models.BooleanField()
    quadrant = models.CharField(max_length=255)
    OD1 = models.DecimalField(max_digits=3, decimal_places=3)
    OD2 = models.DecimalField(max_digits=3, decimal_places=3)
    OD3 = models.DecimalField(max_digits=3, decimal_places=3)
    OD_Avg = models.DecimalField(max_digits=3, decimal_places=3)
    MW_1 = models.DecimalField(max_digits=3, decimal_places=3)
    MW_2 = models.DecimalField(max_digits=3, decimal_places=3)
    MW_3 = models.DecimalField(max_digits=3, decimal_places=3)
    MW_Avg = models.DecimalField(max_digits=3, decimal_places=3)
    ID1 = models.DecimalField(max_digits=3, decimal_places=3)
    ID2 = models.DecimalField(max_digits=3, decimal_places=3)
    ID3 = models.DecimalField(max_digits=3 , decimal_places=3)
    ID_Avg = models.DecimalField(max_digits=3, decimal_places=3)

    



class MTRSurfaceHardness(models.Model):
    test_id = models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    prolongation_surface = models.BooleanField()
    quadrant = models.BooleanField()
    location = models.CharField(max_length=255)
    test_units = models.CharField(max_length=255)




class MTRCharpyImpacts(models.Model):
    test_id = models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    temperature_unit = models.CharField(max_length=5)
    temperature = models.SmallIntegerField()
    impact_unit = models.CharField(max_length=255)
    impact1 = models.CharField(max_length=255)
    impact2 = models.CharField(max_length=255)
    impact3 = models.CharField(max_length=255)
    LAT_EXP_unit = models.CharField(max_length=5)
    LAT_EXP1 = models.SmallIntegerField()
    LAT_EXP2 = models.SmallIntegerField()
    LAT_EXP3 = models.SmallIntegerField()
    Shear_D_F1 = models.SmallIntegerField()
    Shear_D_F2 = models.SmallIntegerField()
    Shear_D_F3 = models.SmallIntegerField()

   

class MTRGrainSize(models.Model):
    test_id = models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    result1 = models.DecimalField(max_digits=3, decimal_places=3)
    result2 = models.DecimalField(max_digits=3, decimal_places=3)
    


class MTRNonDestructiveTesting(models.Model):
    test_id =  models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    astm_a388 = models.BooleanField()
    
    



class MTRMechanicalProperties(models.Model):
    test_id = models.ForeignKey(MTRMaterialTesting, on_delete=models.CASCADE)
    tensile_yield_unit = models.CharField(max_length=5)
    tensile = models.IntegerField()
    yield_2_off = models.IntegerField()
    yield_6_eul = models.IntegerField()
    elong_in_2_percent = models.IntegerField()
    reduction_in_area = models.FloatField()
    yield_strength_ratio = models.FloatField()
    mechanical_properties_notes = models.CharField(max_length=100)

   






