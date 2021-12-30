from django.urls import path
from product.views import add_to_cart, product
from web.views import index, about, subscribe, why, testimonial
from product.views import cart


app_name = 'web'

urlpatterns = [
    path('', index , name="index"),
    path('about/', about , name="about"),
    path('product/', product , name="product"),
    path('why/', why , name="why"),
    path('testimonial/', testimonial , name="testimonial"),
    path('subscribe/', subscribe, name="subscribe"),
    path('cart/', cart, name="cart"),
    path('add_to_cart/<pk>', add_to_cart, name="add_to_cart")

]