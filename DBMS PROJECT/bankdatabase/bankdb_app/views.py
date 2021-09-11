from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render,redirect
from django.contrib.auth.models import  User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from .models import BankBranch,CustomerTable,AccountTable,ContactTable,TransactionTable,EmployeeTable  
from django.contrib.auth.hashers import make_password
flag=False
def adminlogin(request):
    if request.method=='POST':
        admin_id=request.POST['admin_id']
        password=request.POST['password']
        if authenticate(username=admin_id,password=password):
            return redirect('/admin')
        else:
            messages.info(request,'Ínvalid Credentials')
            return redirect('/adminlogin')
    else:
        return render(request,'adminlogin.html')
def managerlogin(request):
    if request.method=="POST":
        manager_id=int(request.POST['manager_id'])
        branch_id=int(request.POST['branch_id'])
        if BankBranch.objects.filter(manager_number=manager_id,branch_id=branch_id): 
            request.session["isManager"] =  True
            context = {
                "isManager":True
            }
            return render(request,'managerloginnext.html', context)
        else:
            flag=0
            messages.info(request,'Invalid Credentials')
            return redirect('managerlogin')
        
    else:    
        return render(request,'managerlogin.html')

def addemployee(request):
    if request.method=='POST':
        manager_id=int(request.POST['manager_id'])
        if BankBranch.objects.filter(manager_number=manager_id):
            bran=BankBranch.objects.get(manager_number=manager_id)
            branch_id=bran.branch_id
        else:
            messages.info(request,'Invalid Manager ID')
            return redirect('/addemployee')
        employee_id=int(request.POST['employee_id'])
        employee_name=request.POST['employee_name']
        employee_gender=request.POST['gender']
        employee_address=request.POST['employee_address']
        employee_phoneno=int(request.POST['employee_phone'])
        employee_email=request.POST['employee_email']
        employee_qualification=request.POST['employee_qualification']
        if BankBranch.objects.filter(branch_id=branch_id):
            if not EmployeeTable.objects.filter(employee_id=employee_id):
                if not EmployeeTable.objects.filter(employee_email=employee_email):
                    employee=EmployeeTable.objects.create(branch_id_id_id=branch_id,employee_id=employee_id,employee_name=employee_name,employee_gender=employee_gender,employee_address=employee_address,employee_phone_no=employee_phoneno,employee_email=employee_email,employee_qualification=employee_qualification)
                    employee.save()
                    return redirect('/managerloginnext')
                else:
                    messages.info(request,'Email ID Exists')
                    return redirect('/addemployee')
            else:
                messages.info(request,'Employee ID Exists')
                return redirect('/addemployee')
        else:
            messages.info(request,'Invalid Bank Branch ID')
            return redirect('/addemployee')
    else:
        return render(request,'addemployee.html')

def employeelogin(request):
    global flag
    flag=False
    if request.method=="POST":
        employee_id=int(request.POST['employee_id'])
        branch_id=int(request.POST['branch_id'])
        if EmployeeTable.objects.filter(employee_id=employee_id,branch_id_id=branch_id):
            request.session["isManager"] =  False
            return redirect('/deposit', {'context': False})
        else:
            messages.info(request,'Invalid credentials')
            return redirect('employeelogin')
    else:        
        return render(request,'employeelogin.html')

def newcustomer(request):
    if request.method=="POST":
        customer_id=int(request.POST['customer_id'])
        customer_name=request.POST['customer_name']
        customer_phone_no=request.POST['customer_phone']
        customer_email=request.POST['customer_email']
        customer_address=request.POST['customer_address']
        if not CustomerTable.objects.filter(customer_id=customer_id):
            if not CustomerTable.objects.filter(customer_email=customer_email):
                customer=CustomerTable.objects.create(customer_id=customer_id,customer_name=customer_name,customer_phone_no=customer_phone_no,customer_email=customer_email,customer_address=customer_address)
                customer.save()
            
                return redirect('/newaccount')
            else:
                messages.info(request,'Email is Already Taken')
                return redirect('/newcustomer')
        else:
            messages.info(request,'Customer ID Exists')
            return redirect('/newcustomer')
    else:
        isManager = request.session["isManager"]
        return render(request,'newcustomer.html', {'context': isManager})

def newaccount(request):
    if request.method=="POST":
        customer_id=int(request.POST['customer_id'])
        your_id=int(request.POST['your_id'])
        if BankBranch.objects.filter(manager_number=your_id):
            bran=BankBranch.objects.get(manager_number=your_id)
            branch_id=bran.branch_id
        elif EmployeeTable.objects.filter(employee_id=your_id):
            empl=EmployeeTable.objects.get(employee_id=your_id)
            branch_id=empl.branch_id_id_id
        else:
            messages.info(request,'Invalid ID')
            return redirect('/newaccount')
        account_type=request.POST['account']
        account_number=int(request.POST['account_number'])
        balance=int(request.POST['Amount'])
        password=request.POST['password']
        if BankBranch.objects.filter(branch_id=branch_id):
            if CustomerTable.objects.filter(customer_id=customer_id):
                if not AccountTable.objects.filter(account_number=account_number):
                    account=AccountTable.objects.create(which_branch_id=branch_id,account_number=account_number,account_type=account_type,balance=balance,customer_number_id=customer_id,account_password=password)
                    account.save()
                    messages.info(request,'Account Created')
                    return redirect ('/newaccount')
                else:
                    messages.info(request,'Account Number Exists')
                    return redirect('/newaccount')
            else:
                messages.info(request,'Customer ID is Invalid')
                return redirect('/newaccount')
        else:
            messages.info(request,'BankBranch ID is Invalid')
            return redirect('/newaccount')
    else:
        
        isManager = request.session["isManager"]
        return render(request,'newaccount.html', {'context': isManager})

def deposit(request):
    if request.method=='POST':
        account_number=int(request.POST['account_number'])
        amount=int(request.POST['amount'])
        try:
            account=AccountTable.objects.get(account_number=account_number)
        except AccountTable.DoesNotExist:
            account=None
        if not account:
            messages.info(request,'Invalid Account Number')
            return redirect('/deposit')
        account.balance+=amount
        account.save()
        customer_id=account.customer_number_id
        trans=TransactionTable.objects.create(trans_account_number_id_id_id=account_number,credit_or_debit="credit",amount=amount,trans_customer_id=customer_id)
        trans.save()
        messages.info(request,'Credited')
        return redirect('/deposit')
    else:
        isManager = request.session["isManager"]
        return render(request,'deposit.html', {'context': isManager})

def withdraw(request):
    if request.method=='POST':
        account_number=int(request.POST['account_number'])
        password=request.POST['password']
        amount=int(request.POST['amount'])
        try:
            account=AccountTable.objects.get(account_number=account_number,account_password=password)
        except AccountTable.DoesNotExist:
            account=None
        if not account:
            messages.info(request,'Invalid Credentials')
            return redirect('/withdraw')
        if account.balance>amount:
            account.balance-=amount
            account.save()
            customer_id=account.customer_number_id
            trans=TransactionTable.objects.create(trans_account_number_id_id_id=account_number,credit_or_debit="debit",amount=amount,trans_customer_id=customer_id)
            trans.save()
            messages.info(request,'Debited')
            return redirect('/withdraw')
        else:
            messages.info(request,"Not Enought of Balance")
            return redirect('/withdraw')
    else:
        isManager = request.session["isManager"]
        return render(request,'withdraw.html', {'context': isManager})

def transfer(request):
    if request.method=='POST':
        from_account_number=int(request.POST['from_account_number'])
        password=request.POST['password']
        to_account_number=int(request.POST['to_account_number'])
        amount=int(request.POST['amount'])
        try:
            accounta=AccountTable.objects.get(account_number=from_account_number,account_password=password)
        except AccountTable.DoesNotExist:
            accounta=None
        if not accounta:
            messages.info(request,'Invalid Credentials')
            return redirect('/transfer')
        try:
            accountb=AccountTable.objects.get(account_number=to_account_number)
        except AccountTable.DoesNotExist:
            accountb=None
        if not accountb:
            messages.info(request,'Invalid Account Number')
            return redirect('/transfer')
        if accounta.balance>amount:    
            accounta.balance-=amount
            accounta.save()
            customer_id=accounta.customer_number_id
            trans=TransactionTable.objects.create(trans_account_number_id_id_id=from_account_number,credit_or_debit="debit",amount=amount,trans_customer_id=customer_id)
            trans.save()
        else:
            messages.info(request,"Not Enought of Balance")
            return redirect('/transfer')
        accountb.balance+=amount
        accountb.save()
        customer_id=accountb.customer_number_id
        trans=TransactionTable.objects.create(trans_account_number_id_id_id=to_account_number,credit_or_debit="credit",amount=amount,trans_customer_id=customer_id)
        trans.save()
        messages.info(request,'Transfer Successful')
        return redirect('/transfer')
    else:
        isManager = request.session["isManager"]
        return render(request,'transfer.html', {'context': isManager})

def closeaccount(request):
    if request.method=='POST':
        account_number=int(request.POST['account_number'])
        customer_number=int(request.POST['customer_number'])
        password=request.POST['password']
        try:
            account=AccountTable.objects.filter(account_number=account_number,customer_number=customer_number,account_password=password)
        except AccountTable.DoesNotExist:
            account=None
        if not account:
            messages.info(request,'Invalid Credentials')
            return redirect('/closeaccount')
        account.delete()
        messages.info(request,'Account Closed Successfully')
        return redirect('/closeaccount')
    else:
        isManager = request.session["isManager"]
        return render(request,'closeaccount.html', {'context': isManager})

def deletecustomer(request):
    if request.method=='POST':
        customer_number=int(request.POST['customer_number'])
        if AccountTable.objects.filter(customer_number=customer_number):
            messages.info(request,'Account exist')
            return redirect('/deletecustomer')
        else:
            if CustomerTable.objects.filter(customer_id=customer_number):
                customer=CustomerTable.objects.get(customer_id=customer_number)
                customer.delete()
                messages.info(request,'Customer Deletion Successful')
                return redirect('/deletecustomer')
            else:
                messages.info(request,'Invalid Customer ID')
                return redirect('/deletecustomer')
    else:
        isManager = request.session["isManager"]
        return render(request,'deletecustomer.html', {'context': isManager})

def deleteemployee(request):
    if request.method=='POST':
        manager_id=int(request.POST['manager_id'])
        employee_id=int(request.POST['employee_id'])
        if BankBranch.objects.filter(manager_number=manager_id):
            bran=BankBranch.objects.get(manager_number=manager_id)
            branch_id=bran.branch_id
        else:
            messages.info(request,'Invalid Manager ID')
            return redirect('/deleteemployee')
        if EmployeeTable.objects.filter(branch_id_id=branch_id):
            if EmployeeTable.objects.filter(employee_id=employee_id):
                try:
                    employee=EmployeeTable.objects.get(branch_id_id=branch_id,employee_id=employee_id)
                except EmployeeTable.DoesNotExist:
                    employee=None
                if not employee:
                    messages.info(request,'Invalid Employee ID')
                    return redirect('/deleteemployee')
                employee.delete()
                return redirect('/managerloginnext')
            else:
                messages.info(request,'Invalid Employee ID')
                return redirect('/deleteemployee')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/deleteemployee')
    else:
        isManager = request.session["isManager"]
        return render(request,'deleteemployee.html', {'context': isManager})

def transactionhistory(request):
    if request.method=="POST":
        account_number=int(request.POST['account_number'])
        if AccountTable.objects.filter(account_number=account_number):
            return transactiondetails(request,account_number)
        else:
            messages.info(request,'Invalid Account Number')
            return redirect('/transactionhistory')
    else:
        isManager = request.session["isManager"]
        return render(request,'transactionhistory.html', {'context': isManager})
def transactiondetails(request,account_number):
    account=TransactionTable.objects.filter(trans_account_number_id_id=account_number)
    # isManager = request.session["isManager"]
    # mm={"isManager":isManager}    
    # #return render(request,'balanceenquiry.html', )
    return render(request,'transactiondetails.html',{'context':account})

def balanceenquiry(request):
    if request.method=='POST':
        customer_number=int(request.POST['customer_number'])
        account_number=int(request.POST['account_number'])
        if AccountTable.objects.filter(customer_number=customer_number,account_number=account_number):
            return balancee(request,account_number)
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/balanceenquiry')
    else:
        isManager = request.session["isManager"]
        return render(request,'balanceenquiry.html', {'context': isManager})
def balancee(request,account_number):
    account=AccountTable.objects.get(account_number=account_number)
    balance=account.balance
    return render(request,'balancee.html',{'account_number':account_number,'balance':balance})

def branchdetails(request):
    if request.method=="GET":
        bankbranch=BankBranch.objects.all()
        return render(request,'branchdetails.html',{'context':bankbranch})

def employeedetails(request):
    if request.method=="GET":
        employee=EmployeeTable.objects.all()
        return render(request,'employeedetails.html',{'context':employee})

def contact(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        country=request.POST['country']
        message=request.POST['message']
        cont=ContactTable.objects.create(contact_first_name=first_name,contact_lastname=last_name,contact_country=country,contact_message=message)
        cont.save()
        return redirect('/home')
    else:
        return render(request,'contact.html')

def home(request):
    return render(request,'home.html') 

def managerloginnext(request):
    return render(request,'managerloginnext.html')

def about(request):
    return render(request,'about.html')




