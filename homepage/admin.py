from django.contrib import admin
from .models import users,contact_form

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "chats", "promptsAnswered")
    search_fields = ("name",)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date")
    list_filter = ("date",)
    search_fields = ("name", "email")
    ordering = ("-date",)

admin.site.register(users, UserAdmin)
admin.site.register(contact_form, ContactFormAdmin)