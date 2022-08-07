from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.views.generic.edit import CreateView
from api.serializers import (UserSerializer, GroupSerializer, UserSerializer,
                            GroupSerializer, GeneralExpenseSerializer,
                            UserDataSerializer, ExpenseCategorySerializer)
from api.models import Expense_category_tbl, User_details_tbl, Expense_summary_tbl, Expense_category_tbl


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class UserDataViewSet(APIView):
    def get(self, request,username):
        queryset = User_details_tbl.objects.filter(user_name=username)
        serializer_data = UserDataSerializer(queryset,many = True)
        return Response(serializer_data.data)

    def post(self,request):
        if 'user_name' in request.data.keys():
            if not User_details_tbl.objects.filter(user_name=request.data['user_name']).exists():
                try:
                    queryset = User_details_tbl(user_name = request.data['user_name'], name = request.data['name'], password = request.data['password'] )
                    queryset.save()
                except:
                    return Response({'status':'Something Went wrong, please check the input data'})
                return Response({'status':'User created Successfully'})
            else:
                return Response({'status':'User Already Exist'})

class ExpenseDataViewSet(APIView):
    def get(self, request,userid):
        # import pdb;pdb.set_trace()
        queryset = Expense_summary_tbl.objects.filter(user_id=userid)
        serializer_data = GeneralExpenseSerializer(queryset,many = True)
        return Response(serializer_data.data)

    def post(self,request,userid):
        # import pdb; pdb.set_trace()
        try:
            discription = request.data['discription']
            amount = request.data['amount']
            # updated_at = request.data['updated_at']
            category_id = request.data['category_id']
        except:
            return Response({'status':"Please send the data in required format"})
        if None in [discription,amount,category_id]:
            return Response({'status':"Please send the data in required format"})

        expense_category = Expense_category_tbl.objects.filter(id=category_id)[0].expense_category
        query = Expense_summary_tbl(Discription = discription,Amount = amount,expense_category=expense_category)
        query.user_id = User_details_tbl.objects.get(id = userid)
        query.category_id = Expense_category_tbl.objects.get(id = category_id)
        query.save()
        return Response({'status':'Expense Added'})

    def put(self,request,userid,expense_id):
        try:
            queryset = Expense_summary_tbl.objects.get(id=expense_id,user_id=userid)
        except Exception as e:
            if 'matching query does not exist' in str(e):
                return Response({'status':'Not Found in DataBase'})
        for key in request.data.keys():
            setattr(queryset,key,request.data[key])
        queryset.save()
        return Response({'status':'Expenses Updated'})

    def delete(self,request,userid,expense_id):
        try:
            queryset = Expense_summary_tbl.objects.get(id=expense_id,user_id=userid)
        except Exception as e:
            if 'matching query does not exist' in str(e):
                return Response({'status':'Not Found in DataBase'})
        queryset.delete()        
        return Response({'status':'Expense Has been Deleted SuccessFully'})



class ExpenseCategoryViewSet(APIView):
    def get(self,request,categoryname):
        if not Expense_category_tbl.objects.filter(expense_category=categoryname).exists():
            return Response({'status':f'{categoryname} Not found'})
        else:
            queryset = Expense_category_tbl.objects.filter(expense_category=categoryname)
            serializer_data = ExpenseCategorySerializer(queryset,many = True)
            return Response(serializer_data.data)

    def post(self,request):
        if Expense_category_tbl.objects.filter(expense_category=request.data['expense_category']).exists():
            return Response({'status':f'Category already Available'})
        if 'color' in request.data.keys():
             query = Expense_category_tbl(expense_category =  request.data['expense_category'], color=request.data['color'])
             query.save()
             return Response({'status':f'Category has been added into database'})
        else:
            query = Expense_category_tbl(expense_category =  request.data['expense_category'])
            query.save()
            return Response({'status':f'Category has been added into database'})
        
        
