from django.contrib import admin
from .models import Mkcrawling, Instagram

#admin.site.unregister(Group)
admin.site.site_header = '기업정보 플랫폼'
admin.site.index_title = '기업정보 플랫폼'
admin.site.register(Mkcrawling)
admin.site.register(Instagram)
