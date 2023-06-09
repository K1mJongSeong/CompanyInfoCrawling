from collections import OrderedDict
from typing import Any, Dict, Optional
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Qna, PuchasedSales, Instagram, User
from .validators import validate_username
from .forms import MyUserForm




admin.site.unregister(get_user_model())
admin.site.unregister(Group)
admin.site.site_header = '기업정보 플랫폼'
admin.site.index_title = '기업정보 플랫폼'

# admin.site.register(Mkcrawling)
#admin.site.register(Instagram)

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username','password')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#     )
#     readonly_fields = ('password_change_link',)

#     def password_change_link(self, obj):
#         url = reverse('admin:auth_user_password_change', args=[obj.pk])
#         return format_html('<a href="{}">비밀번호 변경</a>', url)

#     password_change_link.short_description = '비밀번호 변경'

#     def get_fieldsets(self, request, obj=None):
#         fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
#         if obj:
#             fieldsets = list(fieldsets)
#             fieldsets[0] = (None, {'fields': ('username', 'password_change_link')})
#         return fieldsets
#     list_display = ('username','is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'groups')
#     search_fields = ('username', 'first_name', 'last_name', 'email')
#     ordering = ('username',)

#     def save_model(self, request, obj, form, change):
#         try:
#             validate_username(obj.username)
#         except ValidationError as e:
#             messages.error(request, e.messages[0])
#             form.errors['username'] = e.messages
#             return
#         super().save_model(request, obj, form, change)

#     def response_add(self, request, obj, post_url_continue=None):
#         if "_continue" in request.POST or "_saveasnew" in request.POST:
#             return super().response_add(request, obj, post_url_continue)
#         else:
#             return HttpResponseRedirect(reverse("admin:auth_user_changelist"))

#     def response_change(self, request, obj):
#         if "_continue" in request.POST or "_saveasnew" in request.POST or "_addanother" in request.POST:
#             return super().response_change(request, obj)
#         else:
#             return HttpResponseRedirect(reverse("admin:auth_user_changelist"))


# # # Unregister the default UserAdmin
# #

# # Register the CustomUserAdmin
# admin.site.register(User, CustomUserAdmin)

#admin.site.unregister(User)

class MyUserAdmin(admin.ModelAdmin):
    #fields = ['user_id','name','auth_state','sub_date','last_login']
    list_display = ('user_id','name','auth_state','sub_date','last_login')
    search_fields = ('name','email')
    list_filter = (('sub_date', DateRangeFilter),)
    list_per_page = 8
    #change_list_template = 'admin/account_filter.html'
    # change_form_template = 'admin/account_detail.html'
    form = MyUserForm

    # def get_actions(self, request):
    #     return []

    def has_add_permission(self, request, obj=None):
        # 추가 권한 없애기
        return False
    
admin.site.register(User, MyUserAdmin)


class QnaAdmin(admin.ModelAdmin):
    fields = ['question','question_content','answer','exposure']
    search_fields = ['question','writer'] #질문, 작성자
    list_filter = (('create_at', DateRangeFilter),)
    list_display = ('qna_id','question','answer','exposure','create_at')
    list_per_page = 8

    def has_change_permission(self, request, obj=None):
        if request.path.endswith('/history/'):  # history_view에 대한 요청을 차단합니다.
            return False
        return super().has_change_permission(request, obj)
    #change_list_template = 'admin/qna.html'
    
    # def get_actions(self, request):
    #     return []


admin.site.register(Qna, QnaAdmin)    


class PuchasedSalesAdmin(admin.ModelAdmin):
    list_display = ('ps_id','trans_num','trans_item','trans_name','payment','state','pay_method','trans_date')
    search_fields = ['trans_num','trans_item','trans_name']
    list_display_links = ('trans_name'),
    list_filter = ('trans_date', DateRangeFilter),
    list_per_page = 8
    # change_list_template = 'admin/transaction.html'
    # change_form_template = 'admin/trans_log.html'
    
    # def get_actions(self, request):
    #     return []

    def has_add_permission(self, request, obj=None):
        # 추가 권한 없애기
        return False

    def has_change_permission(self, request, obj=None):
        # 변경 권한 없애기
        return False
    
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    # trans_info = User.objects.get(pk=object_id)
    # obj = self.get_object(request, object_id)
    
    # # info_seq 값과 일치하는 nansu 객체들을 가져옵니다.
    # transaction = User.objects.filter(info_seq=object_id).order_by('-created_at')

    # extra_context = {'transaction': transaction, 'trans_info': obj}
    # return render(request, 'admin/transaction.html', extra_context)


admin.site.register(PuchasedSales, PuchasedSalesAdmin)