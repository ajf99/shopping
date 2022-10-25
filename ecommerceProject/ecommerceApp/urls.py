from django.urls import path
from . import views
app_name='ecommerceApp'
urlpatterns = [
    path('',views.AllProducts,name='AllProducts'),
    path('<slug:c_slug>/',views.AllProducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatdetail')
]
