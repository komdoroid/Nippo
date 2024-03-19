from django.shortcuts import render
from .models import NippoModel

# Create your views here.
def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]

    return render(request, template_name)