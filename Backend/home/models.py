from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

class FingerImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='finger_images')
    finger = models.ImageField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.finger.delete(save=False)
        super().delete(*args, **kwargs)

class FaceImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='face_images')
    face = models.ImageField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.face.delete(save=False)
        super().delete(*args, **kwargs)

@receiver(pre_delete, sender=FingerImage)
def delete_finger_image_file(sender, instance, **kwargs):
    if instance.finger:
        instance.finger.delete(save=False)

@receiver(pre_delete, sender=FaceImage)
def delete_face_image_file(sender, instance, **kwargs):
    if instance.face:
        instance.face.delete(save=False)

@receiver(post_delete, sender=User)
def delete_user_related_images(sender, instance, **kwargs):
    for finger_image in instance.finger_images.all():
        finger_image.delete()
    for face_image in instance.face_images.all():
        face_image.delete()


class PredictImage(models.Model):
    face = models.ImageField(null=True, blank=True)
    finger = models.ImageField(null=True, blank=True)

