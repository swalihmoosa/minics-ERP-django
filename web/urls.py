from django.urls import path
from product.views import add_to_cart, product
from web.views import index, about, subscribe, why, testimonial
from product.views import cart, remove, add_count, minus_count
from user.views import user_login, user_logout, user_signup


app_name = 'web'

urlpatterns = [
    path('', index , name="index"),
    path('about/', about , name="about"),
    path('product/', product , name="product"),
    path('why/', why , name="why"),
    path('testimonial/', testimonial , name="testimonial"),
    path('subscribe/', subscribe, name="subscribe"),
    path('cart/', cart, name="cart"),
    path('add_to_cart/<pk>', add_to_cart, name="add_to_cart"),
    path('remove/<pk>', remove, name="remove"),
    path('add_count/<pk>', add_count, name="add_count"),
    path('minus_count/<pk>', minus_count, name="minus_count"),
    path('user_login/', user_login, name="user_login"),
    path('user_logout', user_logout, name="user_logout"),
    path('user_signup', user_signup, name="user_signup")

]