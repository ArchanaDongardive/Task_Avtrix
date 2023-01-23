from import_export import resources
from app1.models import Product


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
