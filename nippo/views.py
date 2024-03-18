from django.shortcuts import render

# Create your views here.
def nippoListView(request):
    return render(request, "nippo/nippo-list.html")

def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]

    return render(request, template_name)