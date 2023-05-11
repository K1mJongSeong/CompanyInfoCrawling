from django.contrib import admin, messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Mkcrawling, Instagram, Qna
from .validators import validate_username

admin.site.unregister(Group)
admin.site.site_header = '기업정보 플랫폼'
admin.site.index_title = '기업정보 플랫폼'

# admin.site.register(Mkcrawling)
# admin.site.register(Instagram)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username','password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('password_change_link',)

    def password_change_link(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return format_html('<a href="{}">비밀번호 변경</a>', url)

    password_change_link.short_description = '비밀번호 변경'

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
        if obj:
            fieldsets = list(fieldsets)
            fieldsets[0] = (None, {'fields': ('username', 'password_change_link')})
        return fieldsets
    list_display = ('username','is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        try:
            validate_username(obj.username)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            form.errors['username'] = e.messages
            return
        super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if "_continue" in request.POST or "_saveasnew" in request.POST:
            return super().response_add(request, obj, post_url_continue)
        else:
            return HttpResponseRedirect(reverse("admin:auth_user_changelist"))

    def response_change(self, request, obj):
        if "_continue" in request.POST or "_saveasnew" in request.POST or "_addanother" in request.POST:
            return super().response_change(request, obj)
        else:
            return HttpResponseRedirect(reverse("admin:auth_user_changelist"))

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register the CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

class QnaAdmin(admin.ModelAdmin):
    list_display = ('qna_id','question','answer','exposure','create_at')

admin.site.register(Qna, QnaAdmin)    