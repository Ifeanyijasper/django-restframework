from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')

    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators= [validate_title_no_hello,unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            # 'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    

    #This is default create function
    # def create(self, validated_data):
    #     return super().create(validated_data)

    # Custom Create function
    # def create(self, validated_data):
    #     email = validated_data.pop('email')  # To remove field from validated data
    #     obj =  super().create(validated_data)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email') # Similar action for update
    #     return super().update(instance, validated_data)


    
    #Use the function below for SerilizerMethodField
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse( "product-detail", kwargs={"pk":obj.pk}, request=request)

    def get_my_discount(self, obj):
        # if not hasattr(obj,'id'):
        #     return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()