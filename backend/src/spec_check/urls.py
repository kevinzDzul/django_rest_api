"""spec_check URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# list, retrieve,create
url(r'mtrs_list_relations/', views.MTRRelationsListViewSet.as_view(), name='mtrs_list')
url(r'mtrs_retrieve_relations/', views.MTRRelationsDetailViewSet.as_view(), name='mtrs_retrieve')
url(r'mtrs_create_relations/', views.MTRRelationsCreateViewSet.as_view(), name='mtrs_create')
#

router.register(r'mtrs_chemistry', views.MTRChemistryViewSet)
router.register(r'mtrs_heat_treatment_process', views.MTRHeatTreatmentProcessViewSet)
router.register(r'mtrs_heat_material_type', views.MTRMaterialTypeViewSet)
router.register(r'mtrs_sub', views.MTRSubViewSet)
router.register(r'mtrs_heat_treatment',views.MTRHeatTreatmentViewSet)
router.register(r'mtrs_specifications',views.MTRSpecificationsViewSet)
router.register(r'mtrs_customers',views.MTRCustomersViewSet)
router.register(r'mtrs',views.MTRSViewSet)
router.register(r'mtrs_material_testing',views.MTRMaterialTestingViewSet)
router.register(r'mtrs_hardness_sub',views.MTRHardnessSubViewSet)
router.register(r'mtrs_surface_hardness',views.MTRSurfaceHardnessViewSet)
router.register(r'mtrs_charpy_impacts',views.MTRCharpyImpactsViewSet)
router.register(r'mtrs_grain_size',views.MTRGrainSizeViewSet)
router.register(r'mtrs_non_destructive_testing',views.MTRNonDestructiveTestingViewSet)
router.register(r'mtrs_mechanical_properties',views.MTRMechanicalPropertiesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]







