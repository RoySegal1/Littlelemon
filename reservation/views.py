from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Booking,Menu
from .serializers import bookingSerializer,menuSerializer
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class MenuitemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(RetrieveAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    