from django.urls import path,include
from app import views

urlpatterns=[
    path('home/',views.home,name='register'),
    path('reg_form/',views.register,name='reg_form'),
    path('login/',views.user_login,name='login'),
    path('hostels/<slug:hostel_name>/',views.hostel_detail_view,name='hostel'),
    path('login/edit/',views.edit,name='edit'),
    path('login/select/',views.select,name='select'),
    path('logout/',views.logout_view,name='logout'),
    path('reg_form/login/edit/',views.edit,name='update'),
]

