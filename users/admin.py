# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# ما باید فرم‌های پیش‌فرض ادمین را هم سفارشی کنیم
# تا از ایمیل به جای نام کاربری استفاده کنند.
class CustomUserAdmin(UserAdmin):
    # فیلدهایی که در صفحه لیست کاربران نمایش داده می‌شود
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    # فیلدهایی که برای جستجو استفاده می‌شود
    search_fields = ('email', 'first_name', 'last_name',)
    # فیلدهایی که برای فیلتر کردن استفاده می‌شود
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # ترتیب نمایش فیلدها در صفحه ویرایش کاربر
    ordering = ('email',)

    # fieldsets مشخص می‌کند که فیلدها در صفحه ویرایش چگونه گروه‌بندی شوند.
    # ما اینجا 'username' را از تمام بخش‌ها حذف می‌کنیم.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets برای صفحه ساخت کاربر جدید است.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'), # password2 برای تکرار رمز عبور
        }),
    )

admin.site.register(User, CustomUserAdmin)