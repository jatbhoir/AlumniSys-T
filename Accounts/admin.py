from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
	list_display = ('username', 'email', 'grno', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('username', 'email', 'grno')
	readonly_fields = ('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)


