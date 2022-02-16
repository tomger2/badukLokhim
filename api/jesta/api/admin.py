from django.contrib import admin
from .models import Call, Elder, Pro, Son, Profession, Pro


admin.site.register(Elder)
admin.site.register(Son)
admin.site.register(Profession)
admin.site.register(Pro)
admin.site.register(Call)