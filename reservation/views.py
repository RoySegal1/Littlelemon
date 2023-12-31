from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Booking,Menu
from .serializers import bookingSerializer,menuSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class MenuitemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
    
class SingleMenuItemView(RetrieveAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    