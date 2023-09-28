from django.shortcuts import render, HttpResponseRedirect


def PageNotFound(request):
    return render(request, '404.html', status=404)


def PageNotFound500(request):
    return render(request, '500.html', status=500)
