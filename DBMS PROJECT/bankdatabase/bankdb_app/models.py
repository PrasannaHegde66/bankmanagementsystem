from django.db import models
from datetime import datetime

# Create your models here.
class BankBranch(models.Model):
    branch_id=models.PositiveIntegerField(primary_key=True)
    branch_name=models.CharField(max_length=56)
    branch_city=models.CharField(max_length=80)
    branch_country=models.CharField(max_length=50)
    branch_phone=models.CharField(max_length=12)
    manager_number=models.CharField(default=None,max_length=10)


class CustomerTable(models.Model):
    customer_id=models.PositiveIntegerField(primary_key=True) 
    customer_name=models.CharField(max_length=128)
    customer_address=models.CharField(max_length=256)
    customer_phone_no=models.CharField(max_length=14,unique=True)
    customer_email=models.EmailField(max_length=50,unique=True)


class AccountTable(models.Model):
    account_number=models.PositiveIntegerField(primary_key=True)
    SAVINGACCOUNT='SA'
    FIXEDDEPOSITACCOUNT='FDA'
    ACCOUNT_CHOICESS=[
        (SAVINGACCOUNT,'saving account'),
        (FIXEDDEPOSITACCOUNT,'fixed deposit account'),
    ]
    account_type=models.CharField(max_length=4,choices=ACCOUNT_CHOICESS)
    balance=models.PositiveIntegerField()
    which_branch=models.ForeignKey(BankBranch,on_delete=models.CASCADE)
    customer_number=models.ForeignKey(CustomerTable,on_delete=models.CASCADE)



class TransactionTable(models.Model):
    date_time_stamp=models.DateTimeField(default=datetime.now())
    trans_account_number_id_id = models.ForeignKey(AccountTable,on_delete=models.CASCADE)
    credit='credit'
    debit='debit'
    C_D_CHOICES=[
        (credit,"Credit"),
        (debit,"Debit"),
    ]
    credit_or_debit=models.CharField(max_length=10,choices=C_D_CHOICES)
    amount=models.IntegerField()
    trans_customer=models.ForeignKey(CustomerTable,on_delete=models.CASCADE)


class EmployeeTable(models.Model):
    employee_id=models.PositiveIntegerField(unique=True)
    employee_name=models.CharField(max_length=50)
    MALE = 'male'
    FEMALE = 'female'
    OTHERS = 'others'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    employee_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    employee_address=models.CharField(max_length=256)
    employee_phone_no=models.CharField(max_length=14)
    employee_email=models.EmailField(max_length=50,unique=True)
    employee_qualification=models.CharField(max_length=40)
    branch_id_id=models.ForeignKey(BankBranch,default=None,on_delete=models.SET_DEFAULT)


class ContactTable(models.Model):
    contact_first_name=models.CharField(max_length=25)
    contact_lastname=models.CharField(max_length=25)
    contact_country=models.CharField(max_length=30)
    contact_message=models.CharField(max_length=256)




