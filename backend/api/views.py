from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()

#     data = {}
#     if instance:
#         # data = model_to_dict(model_data, fields=['id', 'price','sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request,*arg, **kwarg):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        # data = instance
        return Response(serializer.data)
    return Response({'invalid':"not good data"}, status=400)
