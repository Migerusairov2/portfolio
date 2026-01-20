from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

    # logos = [
    #     "react",
    #     "python",
    #     "django",
    #     "javascript",
    #     "nodejs",
    # ]
    # return render(request, "home.html", {"logos": logos})