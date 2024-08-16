from django.urls import path
from rest_framework import routers
from .views import StakeholderView

router = routers.SimpleRouter()
urlpatterns = router.urls

urlpatterns += [
    path('stakeholders/', StakeholderView.as_view(), name='stakeholder_create'),
]