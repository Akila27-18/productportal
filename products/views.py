from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')

    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(brand__icontains=query))
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if available == 'true':
        products = products.filter(is_available=True)
    elif available == 'false':
        products = products.filter(is_available=False)

    total_results = products.count()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

   return render(request, 'products/product_list.html', {
    'products': products,
    'query': query,
    'min_price': min_price,
    'max_price': max_price,
    'availability': availability,
    'total_results': total_results,
})

