

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import  Group

from .models import CustomUser, Product



from rest_framework import serializers

# customer serializer

class RegisterSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    address =serializers.CharField(required=False, allow_blank=True)
    # phone = serializers.IntegerField(required=False, allow_null=True)

    class Meta:

        model = CustomUser
        fields = ["id", "username", "email", "password", "phone","address", "token"] 
        
    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation.pop("password", None)
        return representation

    def create(self, validated_data):

        user = CustomUser.objects.create_user(**validated_data)
        password=validated_data.pop('password')
        group, created = Group.objects.get_or_create(defaults={"name": "user"})
        group.user_set.add(user)
        return user

    def get_token(self, object):

        user = CustomUser.objects.get(username=object.username)
        token, created = Token.objects.get_or_create(user=user)
        return token.key
    

# product Related

class ProductSerializer(serializers.ModelSerializer):

    is_active = serializers.SerializerMethodField()
    customer = RegisterSerializer(read_only=True)
    customer_id = serializers.IntegerField()

    class Meta:

        model = Product
        fields = ["id", "product_name", "description", "price", "registration_date","is_active", "customer_id", "customer", ]
        depth = 1

    def create(self,validated_data):

        customer_id = validated_data.pop('customer_id')
        customer_obj = CustomUser.objects.get(id=customer_id)
        product = Product.objects.create(customer=customer_obj, **validated_data)
        return product
    
    def get_is_active(self, object):
        
        product_active = Product.objects.filter(id=object.id)
        for active in product_active:
            product_in_active = active.is_active
            print("product_active", product_in_active)
            return product_in_active
    
    