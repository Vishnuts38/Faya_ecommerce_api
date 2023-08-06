from django.urls import path,include
from .Apiviews import registerUser, listUsers, rudUser, ProductCreateView, listProducts, rudProduct
urlpatterns =[
     
        path('user_create/',registerUser.as_view(),name="register/"),
        path('list_user/',listUsers.as_view(),),
        path('rud_user/<pk>/',rudUser.as_view()),#api for reterive update and distory
        # product url
        path('product_create/',ProductCreateView.as_view(),),
        path('product_list/',listProducts.as_view(),),
        path('rud_product/<pk>/',rudProduct.as_view()),#include a partial update and retrive and can inactivate by using patch method and also delete product
        
        
       
        ]