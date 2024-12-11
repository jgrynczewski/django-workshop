from rest_framework import serializers

from forms_and_views_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "subject", "body", "date"]
