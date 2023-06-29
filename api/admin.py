from django.contrib import admin
from .models import *

# Register your models here.

class HeaderAdmin(admin.ModelAdmin):
    ...
    search_fields = ['PageType']

admin.site.register(Header_section, HeaderAdmin)
admin.site.register(Home_client_section)
admin.site.register(Home_overwhelmed_section)
admin.site.register(Home_proposal_section)
admin.site.register(Home_service_section)
admin.site.register(Home_step_process_section)
admin.site.register(Home_happy_customer)
admin.site.register(About_Us)
admin.site.register(About_team)
admin.site.register(About_partner)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Service_why_amorserv)
admin.site.register(Blog_Post_Category)
admin.site.register(Blog_Post)
admin.site.register(Blog_Post_Comment)
admin.site.register(Contact_Enquiries)
admin.site.register(Contact_Info)
admin.site.register(Faq)

