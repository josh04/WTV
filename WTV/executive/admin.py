from django.contrib import admin
from executive.models import Exec
from sortable.admin import SortableAdmin

class ExecAdmin(SortableAdmin):
  list_display_links = ('__unicode__', )
  list_display = SortableAdmin.list_display + ('__unicode__', 'name', 'current_exec')


admin.site.register(Exec, ExecAdmin)
