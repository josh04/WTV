from booking.models import Kit, Spec, Booking
from django.contrib import admin

class KitAdmin(admin.ModelAdmin):
  list_display = ('name', 'amount', 'get_specs')
  list_filter = ['specs']

  def get_specs(self, obj):
    return 'books'

admin.site.register(Kit, KitAdmin)
admin.site.register(Spec)
admin.site.register(Booking)
