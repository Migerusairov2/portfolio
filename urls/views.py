from django.urls import URLPattern, URLResolver, get_resolver
from django.shortcuts import render
from django.conf import settings

def urls_dir(request):
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
    return render(request, 'url.html', context)
