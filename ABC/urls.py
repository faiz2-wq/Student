from django.urls import path
from .views import *

urlpatterns = [
    path("pay/", view_getpaymentdetail),
    path('stu/',view_course), 
    path('stufrm/',view_studenform),  
    path('payfrm/',view_paymentform),
    path('stuimg/<int:sid>/',view_show_student_with_img),
    path('staticmedia/',view_static_media),
]
