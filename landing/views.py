from django.shortcuts import render
from django.http import HttpResponse
from django.urls import URLPattern, URLResolver, get_resolver



def home(request):
    return render(request, "home.html", _get_urls())

    # logos = [
    #     "react",
    #     "python",
    #     "django",
    #     "javascript",
    #     "nodejs",
    # ]
    # return render(request, "home.html", {"logos": logos})


def _get_urls():
    resolver = get_resolver()

    def list_urls(patterns, prefix=''):
        urls = []
        for pattern in patterns:
            if isinstance(pattern, URLPattern):
                url_path = '/' + prefix + str(pattern.pattern)
                url_path = url_path.replace('^', '').replace('$', '')
                urls.append(url_path)
            elif isinstance(pattern, URLResolver):
                urls += list_urls(pattern.url_patterns, prefix + str(pattern.pattern))
        return urls

    all_urls = list_urls(resolver.url_patterns)

    filtered_urls = [u for u in all_urls if not u.startswith('/admin/') and u != '/' and u != '/urls/' ]

    sorted_urls = sorted(filtered_urls)
    context = {'urls': sorted_urls}
    return context
    
