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
        obj = NippoModel(title=title, content=content)
        obj.save()

    return render(request, template_name)

def nippoDetailView(request, pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = NippoModel.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name, ctx)