from django.apps import AppConfig
from tensorflow import keras
from django.conf import settings
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    # try:
    #     print(settings.MODELS_FINGER_PATH)
    #     fingerModel = keras.models.load_model(settings.MODELS_FINGER_PATH)
    # except Exception as e:
    #     raise ModuleNotFoundError