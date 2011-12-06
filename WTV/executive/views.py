from django.shortcuts import render_to_response
from executive.models import Exec
from django.template import RequestContext
import datetime

def current_exec(request):
  executive = Exec.objects.filter(year=datetime.date.today().year)

  return render_to_response('executive/current_exec.html', {'executive': executive }, context_instance=RequestContext(request) )


