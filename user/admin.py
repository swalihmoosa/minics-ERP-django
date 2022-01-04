from django.contrib import admin

from user.models import CustomUser, Customer, Testimonial


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_job', 'customer_image', 'testimonial']

admin.site.register(Customer, CustomerAdmin)


admin.site.register(Testimonial)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'confirm_password']

admin.site.register(CustomUser, CustomUserAdmin)