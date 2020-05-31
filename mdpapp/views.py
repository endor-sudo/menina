from django.shortcuts import render
from .models import Client, Product, Sale, Movement
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ClientForm
from .forms import ProductForm
from .forms import FamilyForm
from .forms import MovementForm
from .forms import SaleForm

def index(request):
    return render(request, 'mdpapp/index.html')

@login_required
def dblists(request):
    return render(request, 'mdpapp/dblists.html')

@login_required
def clients(request):
    """Lists Clients"""
    clients = Client.objects.filter(owner=request.user).order_by('client_name')
    context = {'clients': clients}
    return render(request, 'mdpapp/clients.html', context)

@login_required
def products(request):
    """Lists Products"""
    products = Product.objects.order_by('product_name')
    context = {'products': products}
    return render(request, 'mdpapp/products.html', context)

@login_required
def sales(request):
    """Lists Sales"""
    sales = Sale.objects.order_by('sale_date')
    context = {'sales': sales}
    return render(request, 'mdpapp/sales.html', context)

@login_required
def sale(request, sale_id):
    """Show a single sale and all its movements."""
    sale = Sale.objects.get(id=sale_id)
    """
    #Make sure the sale belongs to the current user.
    if sale.owner != request.user:
        raise Http404
    """
    movements = sale.movement_set.order_by('id')
    context = {'sale': sales, 'movements': movements}
    return render(request, 'mdpapp/sale.html', context)

@login_required
def create(request):
    return render(request, 'mdpapp/create.html')

@login_required
def create_client(request):
    """Create a new client."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClientForm()
    else:
        # POST data submitted; process data. 
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client=form.save(commit=False)
            new_client.owner=request.user
            new_client.save()
            return HttpResponseRedirect(reverse('client_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_client.html', context)

@login_required
def create_family(request):
    """Create a new product family."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FamilyForm()
    else:
        # POST data submitted; process data. 
        form = FamilyForm(request.POST)
        if form.is_valid():
            new_family=form.save(commit=False)
            new_family.owner=request.user
            new_family.save()
            return HttpResponseRedirect(reverse('family_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_family.html', context)

@login_required
def create_product(request):
    """Create a new product."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProductForm()
    else:
        # POST data submitted; process data. 
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_product.html', context)

@login_required
def create_sale(request):
    """Create a new product."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        sale_form = SaleForm()
        movement_form = MovementForm()
    else:
        # POST data submitted; process data. 
        sale_form = SaleForm(request.POST)
        movement_form = MovementForm(request.POST)
        sales=Sale.objects.filter(owner=request.user).all()
        if sale_form.is_valid():
            if movement_form.is_valid():
                #saves sale
                sale_form.save()
                #looks for the sale's id saved above
                for sale in sales:
                    sale_id=sale.id
                #gets the sales instance from the id 
                sale_instance=Sale.objects.filter(owner=request.user).get(id=sale_id)
                #cleans the movement_form to be used as kwargs in the Movement instantiation
                mov_dict=movement_form.cleaned_data
                #instantiates the Movement...
                movement_=Movement(sale=sale_instance, movement_product=mov_dict['movement_product'],
                movement_quantity=mov_dict['movement_quantity'],movement_purchase_price=mov_dict['movement_purchase_price'],
                movement_selling_price=mov_dict['movement_selling_price'])
                #...and saves it
                movement_.save()
            return HttpResponseRedirect(reverse('sale_creation'))
    context = {'sale_form': sale_form, 'movement_form': movement_form}
    return render(request, 'mdpapp/new_sale.html', context)
