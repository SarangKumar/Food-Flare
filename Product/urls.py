from django.urls import path, include


from . import views


urlpatterns = (
    # urls for Product
    path('', views.ProductListView.as_view(), name='Product_product_list'),
    path('product/detail/<slug:Rest_id>/', views.ProductDetailView.as_view(), name='Product_product_detail'),
    # path('hello', views.hello,name="hello"),
    # urls for order
    path('restaurant/product/newdetail/<slug:itemid>', views.NewProductDetailView, name="new_product_details"),
    path('restaurant/<slug:r>', views.restaurant, name='restaurant'),
    path('orders/', views.OrderListView.as_view(), name='Product_order_list'),
    path('order/conformed/', views.order_conform, name='Product_order_conform'),
    path('order/create/<slug:slug>', views.OrderCreateView.as_view(), name='Product_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(), name='Product_order_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
)

