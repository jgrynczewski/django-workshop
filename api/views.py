from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from forms_and_views_app.models import Message
from api.serializers import MessageSerializer


# function-based view
@extend_schema(responses=MessageSerializer)
@api_view(['GET'])
def message_list(request):
    """List all messages."""
    posts = Message.objects.all()
    serializer = MessageSerializer(posts, many=True)
    return Response(serializer.data)


# class-based views
class MessageView(APIView):
    serializer_class = MessageSerializer

    """List all messages."""
    def get(self, request):
        posts = Message.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)


# generic views
class MessageListCreateView(ListCreateAPIView):
    """Create a new message and get all messages that exists."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
