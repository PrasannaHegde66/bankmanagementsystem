from django.contrib import admin
from bankdb_app.models import CustomerTable,TransactionTable,AccountTable,EmployeeTable,ContactTable,BankBranch
# Register your models here.
admin.site.register(CustomerTable)
admin.site.register(TransactionTable)
admin.site.register(AccountTable)
admin.site.register(EmployeeTable)
admin.site.register(ContactTable)
#admin.site.register(DepartmentTable)
admin.site.register(BankBranch)