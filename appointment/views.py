from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from pttrack.views import NoteFormView, NoteUpdate, get_current_provider_type
from pttrack.models import Patient

from .models import Appointment
from .forms import AppointmentForm
import datetime
import collections

def list_view(request):

    # Want to sort the list so earliest dates are first
    appointments = Appointment.objects.filter(clindate__gte=datetime.date.today()).order_by('clindate','clintime')
    d = collections.OrderedDict()
    for a in appointments:
        if a.clindate in d:
            d[a.clindate].append(a)
        else:
            d[a.clindate] = [a]
    return render(request, 'appointment/appointment_list.html',
                  {'appointments_by_date': d})


class AppointmentUpdate(NoteUpdate):
    template_name = "pttrack/form-update.html"
    model = Appointment
    form_class = AppointmentForm
    note_type = "Appointment"
    success_url = "/appointment/list"


class AppointmentCreate(NoteFormView):
    template_name = 'appointment/form_submission.html'
    note_type = "Appointment"
    form_class = AppointmentForm
    success_url = "list"

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.author = self.request.user.provider
        appointment.author_type = get_current_provider_type(self.request)

        appointment.save()

        return HttpResponseRedirect(reverse("appointment-list"))

    def get_initial(self):
        initial = super(AppointmentCreate, self).get_initial()
        pt_id = self.request.GET.get('pt_id', None)
        if pt_id is not None:
            patient = get_object_or_404(Patient, pk=pt_id)
            initial['patient'] = patient

        date = self.request.GET.get('current_date', None)
        if date is not None:
            '''
            If appointment attribute clindate = workup.models.ClinicDate,
            default date could be next clindate.
            For now, the default value will be the next Saturday (including day of)
            '''
            initial['clindate'] = datetime.now()

        return initial