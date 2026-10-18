from rest_framework.serializers import ModelSerializer
from core.models import Pet
from core.models import Adoptions

class PetSerializers(ModelSerializer):
  class Meta :
    model = Pet
    fields = '__all__'

class AdoptionSerializers(ModelSerializer):
  class Meta:
    model = Adoptions
    fields = '__all__'