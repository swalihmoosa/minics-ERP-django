from django.urls import path
from web.views import index, about, product, why, testimonial


app_name = 'web'

urlpatterns = [
    path('', index , name="index"),
    path('about/', about , name="about"),
    path('product/', product , name="product"),
    path('why/', why , name="why"),
    path('testimonial/', testimonial , name="testimonial")
]