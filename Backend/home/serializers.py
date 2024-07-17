from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FingerImage, FaceImage,PredictImage
from .ModalViews import *
class FingerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerImage
        fields = ['id', 'finger']

class FaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceImage
        fields = ['id', 'face']

class UserSerializer(serializers.ModelSerializer):
    finger_images = FingerImageSerializer(many=True, read_only=True)
    face_images = FaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'finger_images', 'face_images']

class UserCreateSerializer(serializers.ModelSerializer):
    finger_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    face_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'finger_images', 'face_images']

    def create(self, validated_data):
        finger_images_data = validated_data.pop('finger_images', [])
        face_images_data = validated_data.pop('face_images', [])
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        for finger_image in finger_images_data:
            img1=FingerImage.objects.create(user=user, finger=finger_image)
            # saveFingerData(img1.finger.path,user.id)
        for face_image in face_images_data:
            img2=FaceImage.objects.create(user=user, face=face_image)
            # train_model(img2.face.path,user.id)
        return user


class PredictImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictImage
        fields = ('id', 'face', 'finger')