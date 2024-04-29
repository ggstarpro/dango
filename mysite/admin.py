from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User
# from mysite.models.account_models import User
from mysite.models.profile_models import Profile
# --- 管理画面でUserを作成するにはここが必要 ---
from mysite.forms import UserCreationForm
# ---------------------------------------

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        }),
    )

    list_display = ['email', 'is_active']
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    add_form = UserCreationForm  # adminでuser作成用に追加
    inlines = (ProfileInline,)  # ProfileモデルはUserモデルとOneToOneで紐づいているので、User情報をみる際に一緒に表示するために追記

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)