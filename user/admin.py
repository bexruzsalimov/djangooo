from django.contrib import admin
from user.models import User, Follow

admin.site.register([User, Follow])
