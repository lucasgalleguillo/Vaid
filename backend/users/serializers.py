from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CandidateDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='Person.User.first_name')
    last_name = serializers.CharField(source='Person.User.last_name')
    disponibility = serializers.CharField(source='Person.disponibility')
    country = serializers.CharField(source='Person.country')
    user_id = serializers.CharField(source='Person.User.id')
    born_date = serializers.DateField(source='Person.born_date')

    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'disponibility', 'country', 'request_date', 'user_id', 'born_date', 'interviewed', 'id']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PersonTagDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTagDetails
        fields = '__all__'

class TaskTagDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTagDetails
        fields = '__all__'

class AssignTagsToPersonSerializer(serializers.Serializer):
    tags = serializers.ListField(child=serializers.IntegerField())
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())

class HeadquarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headquarter
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatus
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    Category = ProductCategorySerializer()
    Status = ProductStatusSerializer()

    class Meta:
        model = Product
        fields = '__all__'

class ProductInventoryDetailsSerializer(serializers.ModelSerializer):
    Product = ProductSerializer()
    
    class Meta:
        model = ProductInventoryDetails
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class EventPersonSerializer(serializers.ModelSerializer):
    Person = PersonSerializer()
    
    class Meta:
        model = EventPersonDetails
        fields = '__all__'

class InvitedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

class TaskPersonDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPersonDetails
        fields = '__all__'