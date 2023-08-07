
from rest_framework.permissions import  AllowAny
from rest_framework import generics
from .serializer import RegisterSerializer, ProductSerializer
from .models import CustomUser, Product
from rest_framework.response import Response
import re
from datetime import datetime, timedelta
# Create your views here.


class registerUser(generics.CreateAPIView):
    
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            response_data = {
                "status": "200",
                "message": "Ok",
                "error_code": "",
                "error_message": "",
                "data": serializer.data,
            }

            return Response(response_data)
        except Exception as e:

            print("error",str(e))
            try:
                error_message = dict((e.__dict__)['detail'])
                error_message_keys = dict((e.__dict__)['detail']).keys()
                print("error_message_keys", error_message_keys)
                lst = []
                for key in error_message_keys:
                    print(error_message[key])
                    pattern = r"string='(.*?)'"
                    match = re.search(pattern, str(error_message[key]))
                    final_error_message = match.group(1)
                    lst.append(final_error_message)
                print(" ".join(lst))
                status_code = getattr(e, 'status_code') 
                error_message_text_format = " ".join(lst)

                response_data = {
                    "status": status_code,  # Or appropriate error status code
                    "message": "Error",
                    "error_code": "",  # Optionally, you can add an error code
                    "error_message": str(error_message_text_format),
                    "data": {},
                }

                return Response(response_data)
            except Exception as error:

                return Response({"error":str(error)})
            
class listUsers(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_queryset(self, *args, **kwargs):

        return CustomUser.objects.filter(groups__name="user")
        # return CustomUser.objects.all()

    def list(self, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            item.pop('token', None)

        response_data = {
            "status": 200,
            "error_code": "",
            "error_message": "",
            "message": "Ok",
            "data": data,
        }

        return Response(response_data)

class rudUser(generics.RetrieveUpdateDestroyAPIView):  
    # authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()

    def retrieve(self, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data.pop('token')
        response_data = {
            "status": 200,
            "error_code": "",
            "error_message": "",
            "message": "Ok",
            "data": data,
        }

        return Response(response_data)
    
    def partial_update(self, request, *args, **kwargs):

        try:

            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()  
            data = serializer.data
            
            del data['token']
            response_data = {
                "status": 200,
                "error_code": "",
                "error_message": "",
                "message": "Ok",
                "data": data,
            }
            return Response(response_data)
        
        except Exception as e:

            try:
                error_message = dict((e.__dict__)['detail'])
                error_message_keys = dict((e.__dict__)['detail']).keys()
                
                print("error_message_keys", error_message_keys)
                lst = []
                for key in error_message_keys:
                    print(error_message[key])
                    pattern = r"string='(.*?)'"
                    match = re.search(pattern, str(error_message[key]))
                    final_error_message = match.group(1)
                    lst.append(final_error_message)
                print(" ".join(lst))
                status_code = getattr(e, 'status_code') 
                error_message_text_format = " ".join(lst)

                response_data = {
                    "status": status_code,  
                    "message": "Error",
                    "error_code": "",  
                    "error_message": str(error_message_text_format),
                    "data": {},
                }

                return Response(response_data)
            
            except Exception as error:

                return Response({"error":str(error)})

    
    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
            "status": 200,
            "error_code": "",
            "error_message": "",
            "message": "User Delete successfully..",
            
        }

        return Response(response_data)
    

# product Related

class ProductCreateView(generics.CreateAPIView):
    
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
       
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.errors)
            self.perform_create(serializer)
            data = serializer.data
            customer_data = data['customer']
            customer_data.pop('token')
            data['customer'] = customer_data

            response_data = {
                "status": "200",
                "message": "Ok",
                "error_code": "",
                "error_message": "",
                "data": data,
            }

            return Response(response_data)
        
        except Exception as e:

            status_code = getattr(e, 'status_code') 
            print("status_code", status_code)

            response_data = {
                    "status": status_code,  
                    "message": "Error",
                    "error_code": "",  
                    "error_message": str(e),
                    "data": {},
                }

            return Response(response_data)

class listProducts(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        
        return Product.objects.all()

    def list(self, *args, **kwargs):

        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            for item in data:
               
                print(item['customer'])
                item['customer'].pop('token', None)
                
            response_data = {

                "status": 200,
                "error_code": "",
                "error_message": "",
                "message": "Ok",
                "data": data,
            }

            return Response(response_data)
        
        except Exception as e:

            status_code = getattr(e, 'status_code') 
            print("status_code", status_code)

            response_data = {

                    "status": status_code,  
                    "message": "Error",
                    "error_code": "",  
                    "error_message": str(e),
                    "data": {},
                }

            return Response(response_data)
        
        
class rudProduct(generics.RetrieveUpdateDestroyAPIView):  
  
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def retrieve(self, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        customer_data = data['customer']
        customer_data.pop('token')
        data['customer'] = customer_data
        response_data = {

            "status": 200,
            "error_code": "",
            "error_message": "",
            "message": "Ok",
            "data": data,
        }

        return Response(response_data)
    
    def partial_update(self, request, *args, **kwargs):

        try:

            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            date_is =(datetime.now().date() - timedelta(days=60))
            if instance.registration_date < date_is:
                print("pass",instance.is_active)
                instance.is_active =False
                
            serializer.save()  
            data = serializer.data
            customer_data = data['customer']
            customer_data.pop('token')
            data['customer'] = customer_data

            response_data = {

                "status": 200,
                "error_code": "",
                "error_message": "",
                "message": "Ok",
                "data": data,
            }

            return Response(response_data)
        
        except Exception as e:

            print("error",e)
            try:

                error_message = dict((e.__dict__)['detail'])
                error_message_keys = dict((e.__dict__)['detail']).keys()
                print("error_message_keys", error_message_keys)
                lst = []
                for key in error_message_keys:
                    print(error_message[key])
                    pattern = r"string='(.*?)'"
                    match = re.search(pattern, str(error_message[key]))
                    final_error_message = match.group(1)
                    lst.append(final_error_message)
                print(" ".join(lst))
                status_code = getattr(e, 'status_code') 
                error_message_text_format = " ".join(lst)

                response_data = {

                    "status": status_code,  
                    "message": "Error",
                    "error_code": "", 
                    "error_message": str(error_message_text_format),
                    "data": {},
                }

                return Response(response_data)
            
            except Exception as error:
                
                return Response({"error":str(error)})

    
    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
            "status": 200,
            "error_code": "",
            "error_message": "",
            "message": "Product Delete successfully..",
            
        }
        return Response(response_data)
    
