from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .forms import HotelForm
# from .models import Hotel
# # Create your views here.


# def hotel_image_view(request):

# 	if request.method == 'POST':
# 		form = HotelForm(request.POST, request.FILES)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('success')
# 	else:
# 		form = HotelForm()
# 	return render(request, 'hotel_image_form.html', {'form': form})


# def success(request):
# 	return render(request,'success.html')
# # Python program to view
# # for displaying images


# def display_hotel_images(request):

# 	if request.method == 'GET':

# 		# getting all the objects of hotel.
# 		Hotels = Hotel.objects.all()
# 		return render(request, 'display_hotel_images.html', {'hotel_images': Hotels})
from django.shortcuts import render

def index(request):
    # Any logic or data retrieval can be done here before rendering the template
    return render(request, 'index.html')
def header(request):
    # Any logic or data retrieval for the about page can be done here
    return render(request, 'header.html')
def footer(request):
    # Any logic or data retrieval for the about page can be done here
    return render(request, 'footer.html')
def product(request):
    # Replace this with your actual logic to retrieve product details
    
    return render(request, 'product.html')

def login_view(request):
    return render(request, 'login.html')
    
def signup_view(request):
    return render(request, 'signup.html')   
  
def about_view(request):
    return render(request, 'about.html')   

  
def blog_view(request):
    return render(request, 'blog.html')   
