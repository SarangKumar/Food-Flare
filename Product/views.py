from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Item
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from .forms import CartItemForm



class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/conformed/'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        return context


    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug__iexact=slug)
        form.instance.product = product
        form.instance.cost = int(form.instance.count) * int(product.price)
        return super(OrderCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order


def order_conform(self):
    return render(self, 'Product/thanks.html')


def restaurant(request, r):
    r = r.upper()
    print(r)
    
    model = Item.objects.filter(link_id=r)
    print(model)
    for item in model:
        print(item.link_id, item.item_price)
    return render(request, 'Product/hello.html', {'object_list': model})


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'Product/cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    '''product = get_object_or_404(Product, pk=product_id)
    form = CartItemForm(request.POST or None, initial={'product': product})

    if request.method == 'POST' and form.is_valid():
        quantity = form.cleaned_data['quantity']
        existing_item = CartItem.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            CartItem.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('view_cart')'''
    form = 'Sanjay'
    product = 'SE'
    return render(request, 'Product/add_to_cart.html', {'form': form, 'product': product})