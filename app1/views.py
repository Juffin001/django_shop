from django.shortcuts import render
from django.http import HttpResponse
from .models import box
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *

def index(request):
    latest_boxes_list = box.objects.order_by("-box_pub_date")[:5]
    # template = loader.get_template("app1/index.html")
    context = {"latest_boxes_list": latest_boxes_list}
    return render(request, "app1/main_page.html", context)
    # return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        item = box.objects.get(pk=id)
    except box.DoesNotExist:
        raise Http404("page does not exist")
    return render(request, "app_item/item_page.html", {"item": item})


def results(request, id):
    response = "U are looking on the box with id %s."
    return HttpResponse(response % id)


def create_item(request):
    errors = []
    form = {}
    if request.POST:
        form['title'] = request.POST.get["title"]
        form['img'] = HotelForm(request.POST, request.FILES)
        form['address'] = request.POST.get["address"]
        form['price'] = request.POST.get["price"]
        if not form['title']:
            errors.append("Заполните название")
        if not form['address']:
            errors.append("Заполните адрес")
        if not form['price'].isdigit():
            errors.append("В цену вводите только цифры (стоимость в рублях)")
        if not form['img'].is_valid():
            form['img'] = HotelForm()
        if not errors:
            new_box = box(
            box_title=form['title'],
            box_image=form['img'],
            box_adress=form['address'],
            box_pub_date=timezone.now(),
            box_price=form['price'],
            )
            new_box.save()
            return HttpResponse('Спасибо за ваше сообщение!')
        '''
        if request.method == 'POST':
            form1 = HotelForm(request.POST, request.FILES)
    
            if form1.is_valid():
                form1.save()
        else:
            form1 = HotelForm()
            '''
    return render(
        request,
        "app1/create_item.html",
        {
            "errors": errors,
            "form": form,
        },
    )
def hotel_image_view(request):
  
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'app1/create_item.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')