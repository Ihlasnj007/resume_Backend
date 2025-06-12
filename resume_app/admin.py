# resume_app/admin.py

from django.contrib import admin
from .models import Summary, Education, Certification, Project

admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Project)
