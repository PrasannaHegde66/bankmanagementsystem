from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('managerlogin',views.managerlogin,name='managerlogin'),
    path('employeelogin',views.employeelogin,name='employeelogin'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('branchdetails',views.branchdetails,name='branchdetails'),
    path('cdw',views.cdw,name='cdw'),
    path('newaccount',views.newaccount,name='newaccount'),
    path('balanceenquiry',views.balanceenquiry,name='balanceenquiry'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('transfer',views.transfer,name='transfer'),
    path('closeaccount',views.closeaccount,name='closeaccount'),
    path('transactionhistory',views.transactionhistory,name='transactionhistory'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('deleteemployee',views.deleteemployee,name='deleteemployee'),
    path('managerloginnext',views.managerloginnext,name='managerloginnext'),
    path('newcustomer',views.newcustomer,name='newcustomer'),
    path('balancee',views.balancee,name='balancee'),
    path('transactiondetails',views.transactiondetails,name='transactiondetails'),
    ]