from django.contrib import admin

from .models import Ldapprovider, Domainname

admin.site.register(Ldapprovider)
admin.site.register(Domainname)
