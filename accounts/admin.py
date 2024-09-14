from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_approved', 'is_specially_approved', 'is_staff', 'is_active']
    list_filter = ['is_approved', 'is_specially_approved', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved', 'is_specially_approved', 'training_hospital')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_approved', 'is_specially_approved', 'training_hospital')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
