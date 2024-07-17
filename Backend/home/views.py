from rest_framework import generics
from django.contrib.auth.models import User
from .models import FingerImage, FaceImage
from .serializers import UserSerializer, UserCreateSerializer, PredictImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .train_model import predict_fingerprint

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class UserPredictView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = PredictImageSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            face_image_path = saved_instance.finger.path  # Assuming 'face' is the field name in PredictImageSerializer
            face_label = predict_fingerprint(face_image_path)
            return Response({
                "face_label": face_label,
                # "finger_label": finger_label
            })
        return Response(serializer.errors)