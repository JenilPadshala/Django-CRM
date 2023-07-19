from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.core.mail import send_mail
# Create your views here.

#class-based views:
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"



def landing_page(request):
    return render(request, "landing.html")



class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    #return HttpResponse("Hello World")
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html",context)



class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)



class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        #TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)




def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST) #returned back the form values
        if form.is_valid():
            form.save()         #saves each value of the form from the cleaned_data dictionary
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request,"leads/lead_create.html", context)









class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")




def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead) #returned back the form values
        if form.is_valid():
            form.save()         #saves each value of the form from the cleaned_data dictionary
            return redirect("/leads")
    context = {
         "lead": lead,
         "form": form
     }
    return render(request, "leads/lead_update.html", context)




class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")


def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#              lead.first_name = form.cleaned_data['first_name']
#             lead.last_name = form.cleaned_data['last_name']
#             lead.age = form.cleaned_data['age']
#             lead.save()
#             return redirect("/leads")

#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)