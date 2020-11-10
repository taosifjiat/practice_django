from django.shortcuts import render
from .models import Friends
# Create your views here.
def show_friends(request):
    friend=Friends.objects.all()
    context={"friends":friend}
    return render(request,'jiat/friends.html',context)
def product_detail(reuest):
    return render(request,'product-detail.html')