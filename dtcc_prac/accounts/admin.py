from accounts.models import Application_form
from django.contrib import admin

# Register your models here.

class Application(admin.ModelAdmin):
     class Meta:
         model=Application_form
admin.site.register(Application_form)


