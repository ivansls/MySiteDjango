from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView, UpdateView
)
from ProjectSite.forms import *
from ProjectSite.models import *


# Create your views here.
def indexStart(request):
    return render(request, 'ProjectSite/index.html')


# Catalog
def getStorePage(request):
    return render(request, 'ProjectSite/Catalog/StorePage.html')


def getFeedback(request):
    return render(request, 'ProjectSite/Catalog/StoreActions/Feedback.html')


class ProductWithDrawal(DetailView):
    model = Product
    template_name = 'ProjectSite/Catalog/StoreActions/ProductWithdrawal.html'
    context_object_name = 'list_card'
    pk_url_kwarg = "id"


class getAddingProduct(CreateView):
    model = Product
    form_class = CardForm
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/AddingProduct.html'
    success_url = reverse_lazy('StoreCatalog')


class DeleteProduct(DeleteView):
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/DeleteProduct.html'
    success_url = reverse_lazy("StoreCatalog")


class UpdateProduct(UpdateView):
    model = Product
    pk_url_kwarg = 'id'
    form_class = CardForm
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/ProductСhange.html'
    success_url = reverse_lazy("StoreCatalog")


class CategoryLst(ListView):
    paginate_by = 2
    model = Category
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/CategoryListView.html'
    context_object_name = 'list_card'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/CategoryDetailView.html'
    context_object_name = 'list_card'
    pk_url_kwarg = "id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        product = Product.objects.filter(category=context.get('list_card'))
        context.update({
            'categ': product
        })
        return context


class TagListView(ListView):
    paginate_by = 2
    model = Tag
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/TagListView.html'
    context_object_name = 'list_card'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/CategoryDetailView.html'
    context_object_name = 'list_card'
    pk_url_kwarg = "id"


class TagCreateView(CreateView):
    model = Tag
    form_class = CardFormTag
    template_name = 'ProjectSite/Catalog/StoreActions/ChildPages/AddingProduct.html'
    success_url = reverse_lazy('StoreCatalog')


class BasketListView(ListView):
    paginate_by = 2
    model = Order_item
    template_name = 'ProjectSite/ShoppingCart/View/ListBasketView.html'
    context_object_name = 'list_card'


class BasketDetailView(DetailView):
    model = Order_item
    template_name = 'ProjectSite/ShoppingCart/View/DetailBasketView.html'
    context_object_name = 'list_card'
    pk_url_kwarg = "id"


class BasketUpdateView(UpdateView):
    model = Order_item
    pk_url_kwarg = 'id'
    form_class = BasketForm
    template_name = 'ProjectSite/ShoppingCart/View/UpdateBasketView.html'
    success_url = reverse_lazy("ListShopingCart")


class BasketDeleteView(DeleteView):
    model = Order_item
    pk_url_kwarg = 'id'
    template_name = 'ProjectSite/ShoppingCart/View/DeleteBasketView.html'
    success_url = reverse_lazy("ListShopingCart")


class BasketCreateView(CreateView):
    model = Product
    form_class = BasketForm
    template_name = 'ProjectSite/ShoppingCart/View/CreateBasketView.html'
    success_url = reverse_lazy('ListShopingCart')


class StoreCatalog(ListView):
    paginate_by = 1
    model = Product
    template_name = 'ProjectSite/Catalog/StoreActions/StoreCatalog.html'
    context_object_name = 'list_card'

    def get_queryset(self):
        print(self.request.GET.get('price'))
        return Product.objects.filter(exist=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.request.GET.get('price'))
        context = super().get_context_data()
        context['tag'] = Tag.objects.all()
        category = Category.objects.all()
        tag = Tag.objects.all()
        context.update({
            'tag': tag,
            'categ': category
        })
        return context


def get_product_by_tag(request, tag):
    products = Product.objects.filter(tag__name=tag)
    context = {
        'list_card': products,
        'tag': Tag.objects.all(),
        'categ': Category.objects.all()
    }
    return render(request, 'ProjectSite/Catalog/StoreActions/StoreCatalog.html', context)


def get_product_by_category(request, category):
    products = Product.objects.filter(category__name=category)
    context = {
        'list_card': products,
        'tag': Tag.objects.all(),
        'categ': Category.objects.all()
    }
    return render(request, 'ProjectSite/Catalog/StoreActions/StoreCatalog.html', context)


# def getStoreCatalog(request, a):
#     cards = Product.objects.all()
#     category = Category.objects.all()
#     tag = Tag.objects.all()
#     return render(request, 'ProjectSite/Catalog/StoreActions/StoreCatalog.html', context={'tag':tag,'categ':category,'list_card': cards, "temp":a})


# Catalog:Child
# def getAddingProduct(request):
#     own_form = CardForm()
#     if request.method == "GET":
#         print(request.GET.get('subject'))
#         print(request.GET.get('content'))
#         if own_form.is_valid():
#             print(own_form.cleaned_data)
#             print("adsdada")
#             new_card = Product(**own_form.cleaned_data)
#             new_card.save()
#
#     elif request.method == "POST":
#         own_form = CardForm(request.POST)
#         print(own_form.data)
#         if own_form.is_valid():
#             tags =own_form.cleaned_data.pop('tag')
#             new_card = Product(**own_form.cleaned_data)
#             new_card.save()
#             new_card.tag.set(tags)
#             print(new_card.tag)
#             new_card.save()
#     context = {
#         'form': own_form
#     }
#     return render(request, 'ProjectSite/Catalog/StoreActions/ChildPages/AddingProduct.html', context)


# def getProductChange(request, a):
#     return render(request, 'ProjectSite/Catalog/StoreActions/ChildPages/ProductСhange.html', context={"temp": a})


# API
def getApi(request):
    return render(request, 'ProjectSite/api/api.html')


def getAddNote(request):
    own_form = ApiAddCardForm()
    if request.method == "GET":
        print(request.GET.get('subject'))
        print(request.GET.get('content'))
        if own_form.is_valid():
            print(own_form.cleaned_data)
            print("adsdada")
            new_card = Category(**own_form.cleaned_data)
            new_card.save()

    elif request.method == "POST":
        own_form = ApiAddCardForm(request.POST)
        print(own_form.data)
        if own_form.is_valid():
            print(own_form.cleaned_data)
            print("adsdada")
            new_card = Category(**own_form.cleaned_data)
            new_card.save()
    context = {
        'form': own_form
    }
    return render(request, 'ProjectSite/api/CRUD/AddNote.html', context)


def getDeleteNote(request):
    return render(request, 'ProjectSite/api/CRUD/DeleteNote.html')


def getEditNote(request):
    return render(request, 'ProjectSite/api/CRUD/EditNote.html')


def getReadNote(request):
    return render(request, 'ProjectSite/api/CRUD/ReadNote.html')


# PersonalAre
def getPersonalAre(request):
    return render(request, 'ProjectSite/PersonalArea/PersonalArea.html')


# ShoppingCart
def getShopingCart(request):
    return render(request, 'ProjectSite/ShoppingCart/Basket.html')
