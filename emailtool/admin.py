from django.contrib import admin

# Register your models here.

# from .models import AudienceMember

# admin.site.register(AudienceMember)

from .models import Survey

admin.site.register(Survey)
from django.contrib import admin
from .models import Campaign

admin.site.register(Campaign)
from .models import Feedback
admin.site.register(Feedback)