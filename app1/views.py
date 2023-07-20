from django.shortcuts import render
from django.http import HttpResponse
from .models import box
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_boxes_list = box.objects.order_by("-box_pub_date")[:5]
    #template = loader.get_template("app1/index.html")
    context = {"latest_boxes_list": latest_boxes_list}
    return render(request, "app1/main_page.html", context)
    #return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        item = box.objects.get(pk=id)
    except box.DoesNotExist:
        raise Http404("page does not exist")
    return render(request, "app_item/item_page.html", {"item": item})

def results(request, id):
    response = "U are looking on the box with id %s."
    return HttpResponse(response % id)