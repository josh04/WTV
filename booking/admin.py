from booking.models import Kit, Spec, Booking
from django.contrib import admin

class KitAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'specs')
    list_filter = ['specs']


admin.site.register(Kit, KitAdmin)
admin.site.register(Spec)
admin.site.register(Booking)
