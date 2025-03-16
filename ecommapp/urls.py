from django.urls import path
from . import views

urlpatterns=[

     #path("",views.index,name='index'),
     #path("product_list/",views.product_list,name='product_list'),

    path('',views.index,name='index'),
    path('category/',views.category,name='category'),      #read
    path('category/create/', views.category_create, name='category_create'),    # Create
    path('category/<int:id>/update/', views.category_update, name='category_update'),  # Update
    path('category/<int:id>/delete/', views.category_delete, name='category_delete'),  #delete  
    path('product_list/', views.product_list, name='product_list'),            # Read
    path('product/<str:p_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),    # Create
    path('product/<str:p_id>/update/', views.product_update, name='product_update'),  # Update
    path('product/<str:p_id>/delete/', views.product_delete, name='product_delete'), #delete
    path('add-to-cart/<str:p_id>/', views.add_to_cart, name='add_to_cart'),   #add to cart=>iew cart
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),   #remove items from cart
    path('cart', views.cart, name='cart'),   #view cart
   


]