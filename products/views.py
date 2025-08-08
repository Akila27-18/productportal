from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product

def product_list(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    availability = request.GET.get('availability')

    products = Product.objects.all()

    # Search
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Filter by price range
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Filter by availability
    if availability:
        products = products.filter(availability=availability)

    total_results = products.count()

    paginator = Paginator(products, 5)  # 5 per page
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': products_page,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'availability': availability,
        'total_results': total_results,
    })
