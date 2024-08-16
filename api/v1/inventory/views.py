from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.conf import settings
from importlib import import_module
from .serializers import StakeHolderSerializer

from accounts.models import Stakeholder
            

class StakeholderView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        name = request.data.get('name')
        address = request.data.get('address')
        phone = request.data.get('phone')
        email = request.data.get('email')
        type = request.data.get('type')
        company_name = request.data.get('company_name')
        
        stakeholder = Stakeholder.objects.create(
            stakeholder_name=name,
            stakeholder_address=address,
            stakeholder_mobile=phone,
            stakeholder_email=email,
            stakeholder_type=type,
            company_name=company_name,
        )
        return Response(
            {
                'message': 'Created successfully',
                'data': StakeHolderSerializer(stakeholder).data
            },
            status=status.HTTP_200_OK
            )
    
    
        