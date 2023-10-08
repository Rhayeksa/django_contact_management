from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect

from .forms import Contact as ContactForm
from .models import Contact as ContactModel

# Create your views here.


def add(request):

    if request.method == "POST":
        data = ContactForm(data=request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
            return redirect(to="contact:index")
    else:
        data = ContactForm()

    return render(request=request, template_name="contact/add.html", context={"data": data})


def delete(request, id):
    ContactModel.objects.filter(id=id).delete()
    return redirect(to="contact:index")


def detail(request, id):
    model = ContactModel.objects.get(id=id)

    data = {
        "form": ContactForm(instance=model),
        "model": model,
    }

    return render(request=request, template_name="contact/detail_by_id/index.html", context={"data": data})


def edit(request, id):
    model = ContactModel.objects.get(id=id)

    if request.method == "POST":
        form = ContactForm(
            data=request.POST,
            files=request.FILES,
            instance=model
        )
        if form.is_valid():
            form.save()
            return redirect(to="contact:detail", id=model.id)
    else:
        form = ContactForm(instance=model)

    return render(request=request, template_name="contact/edit_by_id.html", context={"data": form})


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

    return render(request=request, template_name="contact/index.html", context={"data": data})
