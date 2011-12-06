from booking.models import Kit, KitType, Booking
from django.contrib import admin

class KitAdmin(admin.ModelAdmin):
  list_display = ('serial', 'in_store', 'type')

admin.site.register(Kit, KitAdmin)
admin.site.register(KitType)
admin.site.register(Booking)
