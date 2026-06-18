from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.


@login_required
def index(request):
    item_list=Item.objects.all()
    # item_list=Item.objects.filter(is_deleted=False)
    paginator=Paginator(item_list,3)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    context={
        'item_list':page_obj
    }
    return render(request,"food/index.html",context)


class IndexClassView(ListView):
    model=Item
    template_name="food/index.html"
    context_object_name='item_list'
    

@login_required
def detail(request,id):
    item=Item.objects.get(id=id)
    context={
        'item':item
    }
    return render(request,'food/detail.html',context)


class DetailClassView(DetailView):
    # change <int:id> to <int:pk>
    model=Item
    template_name="food/detail.html"
    context_object_name='item'
    



@login_required
def create_item(request):
    form=ItemForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.instance.user_name=request.user
            form.save()
            return redirect('food:index')
        else:
            print(form.errors['item_price'])
    context={
        'form':form,
        'is_update':False
    }
    return render(request,'food/ItemForm.html',context)

class ItemCreateView(CreateView):
    # no need to pass template_name as it automatically look item_form.html (model_form.html)
    # in Item model define get_absolute _url to redirect 
    model=Item
    fields=['item_name','item_desc','item_price','item_image']

@login_required
def edit_item(request,id):
    item = get_object_or_404(Item, id=id, user_name=request.user)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
            form.save()
            return redirect('food:index')
    context={
        'form':form,
        'is_update':True
    }
    return render(request,'food/Itemform.html',context)


class UpdateItemView(UpdateView):
    # it also looks for item_form.html ..change name using template name suffix it looks for item_update_form.html
    # change id as pk
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name_suffix="_update_form"



def delete_item(request,id):
    item=Item.objects.get(id=id)
    item.delete()
    return redirect('food:index')


class DeleteItemView(DeleteView):
    # it looks for item_confirm_delete.html create it 
    # provide success_url
    model=Item
    success_url=reverse_lazy("food:index")


    