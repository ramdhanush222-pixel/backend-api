from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from .models import User
from .serializers import AppointmentSerializer
from django.core.mail import send_mail
from .models import Payment
import razorpay
import os
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def test_api(request):
    return Response({"message": "Backend is working successfully"})

@api_view(['POST'])
def save_appointment(request):
    serializer = AppointmentSerializer(data=request.data)

    if serializer.is_valid():
        appointment = serializer.save()   # 🔥 get object

        return Response({
            "message": "Appointment saved successfully",
            "id": appointment.id   # ✅ IMPORTANT
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_appointments(request):
    appointments = Appointment.objects.all().values()
    return Response(appointments)

@api_view(['GET'])   #  change this
@api_view(['DELETE'])
def cancel_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return Response({"message": "Deleted successfully"})
@api_view(['POST'])
def register_user(request):
    data = request.data

    if User.objects.filter(email=data.get('email')).exists():
        return Response({"error": "User already exists"}, status=400)

    User.objects.create(
        name=data.get('name'),
        email=data.get('email'),
password = make_password(data.get('password'))
    )

    return Response({"message": "Registered successfully"})
@api_view(['POST'])
def login_user(request):
    data = request.data

    try:
        user = User.objects.get(email=data.get('email'))

        if user.password == data.get('password'):
            return Response({
                "message": "Login success",
                "user": user.email
            })
        else:
            return Response({"error": "Invalid password"}, status=400)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=400)
    
    
@api_view(['POST'])
def make_payment(request):
    data = request.data

    payment = Payment.objects.create(
        name=data.get('name'),
        email=data.get('email'),
        amount=data.get('amount'),
        method=data.get('method'),
        status="Success"
    )

    return Response({"message": "Payment successful"})

@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all().values()
    return Response(payments)    
razorpay_client = razorpay.Client(auth=(
    "rzp_test_SeK9s5djtiNHXi",
    "mms3yrhEivq5d3RDbDfaWbg6"
))
@api_view(['POST'])
def create_order(request):
    amount = int(request.data.get('amount')) * 100

    order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    return Response(order)
@api_view(['GET'])
def test_razorpay(request):
    try:
        order = razorpay_client.order.create({
            "amount": 100,
            "currency": "INR",
            "payment_capture": "1"
        })
        return Response(order)
    except Exception as e:
        return Response({"error": str(e)})
@api_view(['POST'])
def verify_payment(request):
    data = request.data

    print("RECEIVED DATA:", data)  # 🔥 DEBUG

    #  DIRECT SAVE (skip verification for now)
    Payment.objects.create(
       
        name=data.get("name"),
        email=data.get("email"),
        amount=data.get("amount"),
        status="Success"
    )

    return Response({"message": "Payment Saved Successfully"})