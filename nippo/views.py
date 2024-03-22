from django.shortcuts import render
from .models import NippoModel
from .forms import NippoFormsClass

# Create your views here.
def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"
    forms = NippoFormsClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj = NippoModel(title=title, content=content)
        obj.save()

    # if request.POST:
    #     title = request.POST["title"]
    #     content = request.POST["content"]
    #     obj = NippoModel(title=title, content=content)
    #     obj.save()

    return render(request, template_name, ctx)

def nippoDetailView(request, pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = NippoModel.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name, ctx)

def nippoUpdateFormView(request, pk):
    template_name = "nippo/nippo-form.html"
    obj = NippoModel.objects.get(pk=pk)
    initial_values = {"title": obj.title, "content":obj.content}
    form = NippoFormsClass(request.POST or initial_values)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj.title = title
        obj.content = content
        obj.save()
    return render(request, template_name,)