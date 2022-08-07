from django.db import models

# Create your models here.
class Expense_category_tbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    expense_category = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=20,default='#008000')

class User_details_tbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50,null=False)
    name = models.CharField(max_length=150,null=False)
    password = models.CharField(max_length=15,null=False)

class Expense_summary_tbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Expense_category_tbl, on_delete=models.CASCADE, to_field='id')
    expense_category = models.CharField(max_length=200,null=False)
    user_id = models.ForeignKey(User_details_tbl, on_delete=models.CASCADE, to_field='id')
    Discription = models.CharField(max_length=200,null=False)
    Amount = models.FloatField(null=False)
    updated_at =  models.DateTimeField(auto_now_add=True, null=False)