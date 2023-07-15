from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
# Create your views here.
def lead_list(request):
    #return HttpResponse("Hello World")
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html",context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

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