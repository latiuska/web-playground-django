
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):

    #Este mixin requerirá que el usuario sea miembro del staff

    @method_decorator(staff_member_required) #El docorador nos permite no tener que añadir el if, lo reemplaza
    def dispatch(self, request, *args, **kwargs): #Seguridad para que solo las personas autorizadas puedan crear o modificar info
        #if not request.user.is_staff:
            #return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page
    

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

    #def get_success_url(self): #Esta es una opción pero se puede hacer con reverse_lazy
        #return reverse ('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy ('pages:update', args=[self.object.id]) + '?ok'
    

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    
    #success_url = reverse_lazy('pages:pages')

    
    
    