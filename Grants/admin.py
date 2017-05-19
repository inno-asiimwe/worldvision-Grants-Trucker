from django.contrib import admin
from . models import Donor, SupportOffice, Expenditure, Payment, Project

# Register your models here.
class DonorInline(admin.TabularInline):
    model = Donor
    Extra = 2

class ExpenditureInline(admin.TabularInline):
    model = Expenditure
    extra = 2

class PaymentInline(admin.TabularInline):
    model = Payment
    Extra = 2




class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'support_office','start_date', 'end_date', 'grant_amount', 'get_status')
    list_filter = ['start_date']
    search_fields = ['project_name', 'support_office', 'support_office']

    fieldsets = [
     (None, {'fields':['project_name','project_identifier', 'support_office', 'description', 'grant_amount'] }),
     ('Date Information', {'fields':['start_date', 'end_date'], 'classes':['collapse']})]

    inlines = [DonorInline, ExpenditureInline, PaymentInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Expenditure)
admin.site.register(Payment)
