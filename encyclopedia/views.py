from django.shortcuts import render, redirect
from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = title + " DOES NOT EXIST"
    if util.get_entry(title) is not None:
        content = markdown(util.get_entry(title))

    if "history" not in request.session:
        request.session["history"] = []
    request.session["history"] += [title]

    return render(request, "encyclopedia/page.html", {
        "name": title,
        "content": content
    })


def search(request):
    t = request.GET.get('q', ' ')
    tmp = util.list_entries()
    if t in util.list_entries():
        return entry(request, t)
    entries = []
    for e in tmp:
        if t in e.lower():
            entries.append(e)
    return render(request, "encyclopedia/listSearch.html", {
        "entries": entries
    })


def history(request):
    if "history" not in request.session:
        request.session["history"] = []
    return render(request, "encyclopedia/history.html", {
        "entries": request.session["history"]
    })


def saveEntry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title,content)
    return render(request, "encyclopedia/saveEntry.html", {})
