from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from .documents import (
    BookDocument
)

def index(request):
    q = request.GET.get("q",None)
    context = {}
    if q is not None:
        query = MultiMatch(query=q, fields=["title", "description"], fuzziness="AUTO")
        books = BookDocument.search().query(query)
        context['books'] = books
    return render(request, 'index.html',context)
