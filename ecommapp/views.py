from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from  . models import Cart, CartItem, Product ,Category
from . forms import ProductForm ,CategoryForm

def index(request):
    return render(request,"index.html")


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')  # Redirect to a category page or another view
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, id=id)  # Use the correct model name
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')  # Ensure 'category' is the correct name in urls.py
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, id): 
   category = get_object_or_404(Category, id=id)
   if request.method == 'POST':
        category.delete()
        
        return redirect('category')
   else:
        return render(request, 'category_delete.html', {'category':category})


# View to list all categories
def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})



def product_list(request): # landing page
    products = Product.objects.all()
    
    return render(request,'product_list.html',{'products': products})

def product_detail(request, p_id):
    product = get_object_or_404(Product, p_id=p_id)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):  #Create the product
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)#request.FILES used for image handling.  
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, p_id):  #Update the product
    products = get_object_or_404(Product, p_id=p_id)
    if request.method == 'POST':
        #form = ProductForm(request.POST, instance=products)#instance load the stored data ,,old code wrong
        form = ProductForm(request.POST, request.FILES, instance=products)# corrected by ajesh
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=products)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, p_id):  # Delete the product
    product = get_object_or_404(Product, p_id=p_id)
    if request.method == 'POST':
        product.delete()
        
        return redirect('product_list')
    else:
     return render(request, 'product_delete.html', {'product':product})

def add_to_cart(request, p_id):
    if not request.user.is_authenticated:
        return redirect('login') 
    product = get_object_or_404(Product, p_id=p_id)
    
    # Use the logged-in user's cart, or create one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Get or create a cart item for the product
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    
    # Increment quantity by 1
    cart_item.quantity += 1
    cart_item.save()
    
    # Add the cart item to the cart
    cart.items.add(cart_item)
    
    # Redirect to the cart page
    return redirect('cart')


def remove_from_cart(request, item_id):
    # Get the cart item by ID, ensuring it's associated with the logged-in user's cart
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    # Delete the cart item
    cart_item.delete()
    
    # Redirect to the cart page
    return redirect('cart')


def cart(request):
    # Get or create the cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Pass the cart to the template
    return render(request, 'cart.html', {'cart': cart})
