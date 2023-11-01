from django.contrib import admin

# Register your models here.
class MyAdminSite(admin.AdminSite):
    login_template = "login.html"

admin_site = MyAdminSite()