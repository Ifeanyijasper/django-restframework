from django.urls import path
from . import views


urlpatterns = [
#     path('', views.ProductMixinView.as_view()),
#     path('<int:pk>/', views.ProductMixinView.as_view()),
#     path('<int:pk>/update/', views.ProductMixinView.as_view()),
#     path('<int:pk>/delete/', views.ProductMixinView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),

    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
]