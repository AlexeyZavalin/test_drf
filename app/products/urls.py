from django.urls import include, path
from rest_framework import routers
from products import views as product_views

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'categories', product_views.CategoriesViewSet)
router.register(r'products', product_views.ProductsViewSet, basename='product-list')
router.register(r'establishments', product_views.EstablishmentViewSet, basename='establishment-list')
router.register(r'menu', product_views.MenuViewSet)
router.register(r'kitchens', product_views.KitchenViewSet)
router.register(r'reviews', product_views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('reviews/<slug:str>', product_views.ReviewList.as_view()),
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework'))
]
