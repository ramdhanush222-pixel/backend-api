from django.urls import path
from .views import test_api, save_appointment, get_appointments, cancel_appointment, make_payment,get_payments,create_order,verify_payment,test_razorpay
from .views import register_user, login_user

urlpatterns = [
    path('test/', test_api),
    path('save/', save_appointment),
    path('appointments/', get_appointments),
    path('delete/<int:id>/', cancel_appointment),
    path('register/', register_user),
    path('login/', login_user),
    path('payment/', make_payment),
    path('payments/', get_payments),
    path('create-order/', create_order),
    path('verify-payment/', verify_payment),
    path('test-razorpay/', test_razorpay),
  
]
