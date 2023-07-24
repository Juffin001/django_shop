from django.shortcuts import render
from django.http import HttpResponse
from .models import box
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

def index(request):
    latest_boxes_list = box.objects.order_by("-box_pub_date")
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
    '''
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
        if request.method == 'POST':
            form1 = HotelForm(request.POST, request.FILES)
    
            if form1.is_valid():
                form1.save()
        else:
            form1 = HotelForm()
            '''
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)
        if form.is_valid():
            #form.box_pub_date = timezone.now()
            form.save()
            return redirect('index')
    else:
        form = BoxForm()
    return render( request, "app1/create_item.html", {'form' : form})


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

def register(request):
    pass

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'app1/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "app1/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('index')
    
def logout_user(request):
    logout(request)
    return redirect('index')

def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = box.objects.filter(box_title__contains=searched)
        return render(request, 'app1/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'app1/search_results.html', {})