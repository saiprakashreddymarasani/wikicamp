# Create your views here.
import markdown

from django.shortcuts import render, HttpResponseRedirect
from .models import Page, Tag
from .forms import SearchForm

def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        tags = page.tags.all()
    except Page.DoesNotExist:
        return render(
            request,
            "appwiki/create.html",
            { 'page_name': page_name }
        )
    content = page.content
    return render(
        request,
        "appwiki/view.html",
        {'page_name': page_name, 'content': markdown.markdown(content), 'tags': tags}
    )

def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
        tags = ' '.join([tag.name for tag in page.tags.all()])
    except Page.DoesNotExist:
        content = ""
        tags = []         
    return render(
        request,
        "appwiki/edit.html",
        { 'page_name': page_name, 'content': content, 'tags': tags }
    )

def save_page(request, page_name):
    content = request.POST['content']
    if 'tags' in request.POST and request.POST['tags']:
        tags = request.POST['tags']
        tag_list = [Tag.objects.get_or_create(name=tag)[0] for tag in tags.split()]
    try:
        page = Page.objects.get(pk=page_name)
        page.content = content
        for tag in tag_list:
            page.tags.add(tag)
    except Page.DoesNotExist:
        page = Page.objects.create(name=page_name, content=content)
    page.save()
    return HttpResponseRedirect('/wikicamp/' + page_name + '/')

def search_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pages = Page.objects.filter(name__icontains=cd['text'])
            contents = []
            if cd['search_content']:
                contents = Page.objects.filter(content__icontains=cd['text'])
            return render(
                request,
                "appwiki/search.html",
                {'form': form, 'pages': pages, 'contents': contents}
            )
    form = SearchForm()
    return render(
        request,
        "appwiki/search.html",
        {'form': form}
    )

def tag_page(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    pages = tag.page_set.all()
    return render(
        request,
        "appwiki/tags.html",
        {'tag_name': tag_name, 'pages': pages}
    )
