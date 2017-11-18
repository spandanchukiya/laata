from products.models import Product

name = 'user'
for i in range(1, 11):
    user = user+i
    product = Product.objects.create(name = user)
