from django.contrib import admin
from django.urls import path
from TestApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('customer', views.showCustomer, name="show-customer"),
    path('add-cust', views.addCust, name="add-cust"),
    path('edit-cust/<str:pk>', views.editCust, name="edit-cust"),
    path('delete-cust/<str:pk>', views.deleteCust, name="delete-cust"),

    path('payment', views.showPayment, name="show-payment"),
    path('add-pay', views.addPayment, name="add-payment"),
    path('edit-pay/<str:pk>', views.editPayment, name="show-payment"),
    path('delete-pay/<str:pk>', views.deletePayment, name="delete-payment"),
    path('print/<str:pk>', views.printInvoice, name="Print-Invoice"),
]