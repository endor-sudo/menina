from django.shortcuts import render
from .models import Client, Product, Sale, Movement
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory, inlineformset_factory

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import ClientForm
from .forms import ProductForm
from .forms import FamilyForm
from .forms import MovementForm
from .forms import SaleForm


import datetime

from django.db.models import Sum

import math

import pygal

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
    """render chart"""
    """
    today=datetime.datetime.now()
    sales = Sale.objects.order_by('sale_date')
    days=[x for x in range(31)]
    bar=[]
    for day in days:
        check_day=today.day
        check_month=today.month
        check_year=today.year
        try:
            check_day=check_day-day
            if check_day<=0:
                check_day+=31
                check_month=check_month-1
                if check_month<=0:
                    check_month=12
                    check_year=check_year-1
            datetime.datetime(year=today.year, month=check_month, day=check_day)
        except ValueError:
            pass
        else:
            total_day=Sale.objects.order_by('sale_date').filter(sale_date__year=check_year).filter(sale_date__month=check_month).filter(sale_date__day=check_day).aggregate(Sum('sale_total'))
            bar.append(total_day['sale_total__sum'])

    bar2=[]
    for data in reversed(bar):
        bar2.append(data)
    print(bar2)

    bar_chart = pygal.Bar()
    bar_chart.add('Últimos mês', bar2)
    bar_chart.render_to_file('mdpapp/static/mdpapp/bar_chart.svg')
    """
    """Lists Sales"""
    today=datetime.datetime.now()
    ##### negative indexing is not supported so this is just a workaround to show the last 5 sales
    sales = Sale.objects.order_by('-sale_date')[:5]
    #####
    year_sale=Sale.objects.filter(sale_date__year=today.year)
    year_sale_total=0
    for sale in year_sale:
        year_sale_total+=float(sale.sale_total)
    #
    month_sale=year_sale.filter(sale_date__month=today.month)
    month_sale_total=0
    for sale in month_sale:
        month_sale_total+=float(sale.sale_total)
    #
    day_sale=month_sale.filter(sale_date__day=today.day)
    day_sale_total=0
    for sale in day_sale:
        day_sale_total+=float(sale.sale_total)
    #
    year_sale_total=round(year_sale_total,2)
    month_sale_total=round(month_sale_total,2)
    day_sale_total=round(day_sale_total,2)
    hoje=today.day
    mes=today.month
    context = {'sales': sales, 'year_sale_total':year_sale_total, 'month_sale_total':month_sale_total, 
    'day_sale_total':day_sale_total, 'hoje':hoje, 'mes':mes}
    return render(request, 'mdpapp/sales.html', context)

@login_required
def todays_sales(request, dia, page):
    today=dia
    todaysales = Sale.objects.order_by('-sale_date').filter(sale_date__day=today)
    bunches=math.ceil(len(todaysales)/5)
    end=5*page
    start=end-5
    todaysales=todaysales[start:end]
    context = {'todaysales': todaysales, 'today':today, 'range':range(1,bunches+1)}
    return render(request, 'mdpapp/allsalestoday.html', context)

@login_required
def months_sales(request, month):
    today=datetime.datetime.now()
    monthsales = Sale.objects.order_by('-sale_date').filter(sale_date__month=month)
    days_total={}
    i=0
    for i in range(1,32):
        day_total=monthsales.filter(sale_date__day=i).aggregate(Sum('sale_total'))
        if day_total['sale_total__sum']:
            days_total[i]=day_total['sale_total__sum']
    print('days_total')
    print(days_total)
    mes=month
    ano=today.year
    context = {'days_total': days_total, 'mes':mes, 'ano':ano}
    return render(request, 'mdpapp/allsalesmonth.html', context)

@login_required
def years_sales(request):
    today=datetime.datetime.now()
    yearsales = Sale.objects.order_by('-sale_date').filter(sale_date__year=today.year)
    days_total={}
    i=0
    for i in range(1,13):
        dia=yearsales.filter(sale_date__month=i)
        day_total=dia.aggregate(Sum('sale_total'))
        if day_total['sale_total__sum']:
            days_total[i]=day_total['sale_total__sum']
    ano=today.year
    context = {'days_total': days_total, 'ano':ano}
    return render(request, 'mdpapp/allsalesyear.html', context)

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
    context = {'sale': sale, 'movements': movements}
    return render(request, 'mdpapp/sale.html', context)

@login_required
def edit_sale(request, sale_id):
    """Edit or delete movements in a sale"""
    #determines sale instance 
    sale = Sale.objects.get(id=sale_id)
    #fabricates the form
    movement_formset = modelformset_factory(Movement, exclude=('sale',), extra=0)
    if request.method!='POST':
        formset = movement_formset(queryset=sale.movement_set.all())
        context = {'formset': formset, 'sale':sale}
        return render(request, 'mdpapp/edit_sale.html', context)
    else:
        #populates the formset
        formset = movement_formset(request.POST, request.FILES, queryset=Movement.objects.none())
        formset.is_valid()

        #checks for blanks before deleting the outdate movements
        for form in formset:
            try:
                mov_dict=form.cleaned_data
                #instantiates the Movement...
                movement_=Movement(sale=sale, movement_product=mov_dict['movement_product'],
                movement_quantity=mov_dict['movement_quantity'],
                movement_purchase_price=mov_dict['movement_purchase_price'],
                movement_selling_price=mov_dict['movement_selling_price'])
            except KeyError:
                return HttpResponseRedirect(reverse('edit_sale', args=[sale.id]))

        #grabs the outdated movements
        old_movs=sale.movement_set.all()
        #and deletes them
        for old_mov in old_movs:
            old_mov.delete()
        for form in formset:
            mov_dict=form.cleaned_data
            #instantiates the Movement...
            movement_=Movement(sale=sale, movement_product=mov_dict['movement_product'],
            movement_quantity=mov_dict['movement_quantity'],
            movement_purchase_price=mov_dict['movement_purchase_price'],
            movement_selling_price=mov_dict['movement_selling_price'])
            movement_.save()

        #updates sale total
        sale_total=[]
        for form in formset:
            #cleans the movement_form to be used as kwargs in the Movement instantiation
            mov_dict=form.cleaned_data
            try:
                sale_total.append(float(mov_dict['movement_quantity'])*float(mov_dict['movement_selling_price']))
            except KeyError:
                pass
        sale.sale_total=round(sum(sale_total),3)
        #saves sale
        sale.save()

        return HttpResponseRedirect(reverse('sales'))

@login_required
def delete_sale(request, sale_id):
    """Delete a sale"""
    #determines sale instance 
    sale = Sale.objects.get(id=sale_id)
    sale.delete()
    return HttpResponseRedirect(reverse('sales'))

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
    movement_formset = modelformset_factory(Movement, exclude=('sale',), extra=1)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        sale_form = SaleForm()
        formset=movement_formset(queryset=Movement.objects.none())
        context = {'sale_form': sale_form, 'formset': formset}
    else:
        # POST data submitted; process data. 
        sale_form = SaleForm(request.POST)
        formset = movement_formset(request.POST,request.FILES, queryset=Movement.objects.none())
        context = {'sale_form': sale_form, 'formset': formset}
        sales=Sale.objects.all()#sales=Sale.objects.filter(owner=request.user).all()
        if sale_form.is_valid() and formset.is_valid():
            saleprov=sale_form.save(commit=False)
            sale_total=[]
            for form in formset:
                #cleans the movement_form to be used as kwargs in the Movement instantiation
                mov_dict=form.cleaned_data
                try:
                    sale_total.append(float(mov_dict['movement_quantity'])*float(mov_dict['movement_selling_price']))
                except KeyError:
                    pass
            saleprov.sale_total=round(sum(sale_total),2)
            #saves sale
            saleprov.save()
            #looks for the sale's id saved above
            for sale in sales:
                sale_id=sale.id
            #gets the sales instance from the id 
            sale_instance=Sale.objects.get(id=sale_id)
            it=0
            for form in formset:
                #cleans the movement_form to be used as kwargs in the Movement instantiation
                mov_dict=form.cleaned_data
                try:
                    #instantiates the Movement...
                    movement_=Movement(sale=sale_instance, movement_product=mov_dict['movement_product'],
                    movement_quantity=mov_dict['movement_quantity'],
                    movement_purchase_price=mov_dict['movement_purchase_price'],
                    movement_selling_price=mov_dict['movement_selling_price'])
                except KeyError:
                    if it==0:
                        sale_instance.delete()
                        #adicionar a nota de que não podem haver vendas sem produtos
                        return HttpResponseRedirect(reverse('sale_creation'))
                #...and saves it
                movement_.save()
                it+=1
            return HttpResponseRedirect(reverse('sale_creation'))
    return render(request, 'mdpapp/new_sale.html', context)