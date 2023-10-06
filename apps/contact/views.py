from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect

from .forms import Contact as ContactForm
from .models import Contact as ContactModel

# Create your views here.


def add(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(to="contact:index")

    return render(request=request, template_name="contact/add.html", context={"form": form})


def delete(request, id):
    return render(request=request, template_name=None, context={})


def detail(request, id):
    return render(request=request, template_name="contact/detail_by_id.html", context={})


def edit(request, id):
    return render(request=request, template_name="contact/edit_by_id.html", context={})


def index(request):
    model = ContactModel.objects.all().order_by("-id")
    page = request.GET.get("page", 1)

    paginator = Paginator(object_list=model, per_page=5)

    try:
        data = paginator.page(number=page)
    except PageNotAnInteger:
        data = paginator.page(number=1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request=request, template_name="contact/index.html", context={"data": model})
