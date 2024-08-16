from rest_framework import serializers
from accounts.models import Stakeholder


class StakeHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = ('id', 'stakeholder_id', 'stakeholder_name', 'stakeholder_address', 'stakeholder_mobile', 'stakeholder_email', 'stakeholder_type')