from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Expense_category_tbl, User_details_tbl, Expense_summary_tbl


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GeneralExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense_summary_tbl
        fields = ['id','category_id','user_id','Discription','Amount','updated_at']


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_details_tbl
        fields = ['id','user_name','name','password']

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense_category_tbl
        fields = ['id','expense_category','color']