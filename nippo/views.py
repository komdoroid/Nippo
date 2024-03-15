from django.shortcuts import render

# Create your views here.
def nippoListView(request):
    return render(request, "nippo/nippo-list.html")