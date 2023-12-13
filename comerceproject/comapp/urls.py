# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import hotel_image_view
# from .views import success
# from .views import display_hotel_images

# urlpatterns = [
# 	path('image_upload', hotel_image_view, name='image_upload'),
# 	path('success', success, name='success'),
# 	path('hotel_images', display_hotel_images, name = 'hotel_images'),
# ]

# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL,
# 						document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import index, header, footer,product

from . import views
urlpatterns = [
    path('', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
	path('product/', views.product, name='product'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    
    # Add more URL patterns as needed
]
