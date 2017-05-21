from django.contrib import admin
from . models import Donor, SupportOffice, Expenditure, Payment, Project

# Register your models here.
class DonorInline(admin.TabularInline):
    model = Donor
    Extra = 2

class ExpenditureInline(admin.TabularInline):
    """In line for Expenditure using the Tabular layout"""
    model = Expenditure
    extra = 2

class PaymentInline(admin.TabularInline):
    """Inline for Payment using the tabular layout"""
    model = Payment
    Extra = 2


class ProjectAdmin(admin.ModelAdmin):
    """Customising the admin area for project  """
    list_display = ('project_name', 'support_office','start_date', 'end_date', 'grant_amount', 'get_status')
    list_filter = ['start_date']
    search_fields = ['project_name']

    fieldsets = [
     (None, {'fields':['project_name','project_identifier', 'support_office', 'description', 'grant_amount'] }),
     ('Date Information', {'fields':['start_date', 'end_date'], 'classes':['collapse']})]

    inlines = [DonorInline, ExpenditureInline, PaymentInline]

class ExpenditureAdmin(admin.ModelAdmin):
    """customising the admin area for project """
    list_display = ('expenditure_text', 'exp_date', 'amount_spent', 'project' )
    list_filter = ['exp_date']
    search_fields = ['expenditure_text', 'exp_date', 'amount_spent', 'project']

class PaymentAdmin(admin.ModelAdmin):
    """Customising Admin area list for payments"""
    list_display = ('payment_text', 'pay_date', 'amount_paid', 'project')
    list_filter = ['pay_date']
    search_fields = ['payment_text', 'pay_date', 'project', 'amount_paid']




admin.site.register(Project, ProjectAdmin)
admin.site.register(Expenditure, ExpenditureAdmin)
admin.site.register(Payment, PaymentAdmin)
