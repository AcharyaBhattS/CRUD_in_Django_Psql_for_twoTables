from django.shortcuts import render, redirect
# from django.db.models.sql.datastructures import Join
from .models import Customer, Payment
from django.contrib import messages
from datetime import datetime
import os


# Display Customer Data
def index(request):
    return render(request, 'index.html')

#__Customer_________________________________________________________________________CUSTOMER____
# Display Customer Data
def showCustomer(request):
    customerDetails = Customer.objects.all()
    context = {'cust_details':customerDetails}
    return render(request, 'customerTable.html', context)

# Insert Customer Data
def addCust(request):
    if request.method == "POST":
        custTableData = Customer()
        CustCode = request.POST.get('cust_code')
        print("CustName: ", CustCode)
        CustName = request.POST.get('cust_name')
        print("CustName: ", CustName)
        customer_room_no = request.POST.get('cust_room_no')
        print("customer_room_no: ", customer_room_no)
        try:
            custTableData.customer_code = CustCode
            custTableData.customer_name = CustName
            custTableData.customer_room_no = customer_room_no
            custTableData.save()
            messages.success(request, "Customer Added Successfully.")
            return redirect('/crud/customer')
        except:
            messages.error(request, "Enter proper information.")
    return render(request, 'addCustomer.html')


def editCust(request, pk):
    custTableData = Customer.objects.get(customer_id=pk)
    if request.method == "POST":
        try:
            custTableData.customer_code = request.POST.get('cust_code')
            custTableData.customer_name = request.POST.get('cust_name')
            custTableData.customer_room_no = request.POST.get('cust_room_no')
            custTableData.save()
            messages.success(request, "Customer Updated Successfully")
            return redirect('/crud/customer')
        except:
            messages.error(request, "Enter proper information.")

    context = {'cust':custTableData}
    return render(request, 'editCustomer.html', context)


def deleteCust(request, pk):
  custTableData = Customer.objects.get(customer_id=pk)
  custTableData.delete()
  messages.error(request, "Record Deleted")
  return redirect('/crud/customer')



#__Payment___________________________________________________________________PAYMENT____
# Display Payment Data
def showPayment(request):
    PaymentTable = Payment.objects.all()
    context = {'pay_details':PaymentTable}
    return render(request, 'paymentTable.html', context)



# Insert Payment Data
def addPayment(request):
    customerDetails = Customer.objects.all()
    context = {'cust_details':customerDetails}
    
    if request.method == "POST":
        SelectedCustomerID = request.POST.get('selectcustomer')
        print("\nSelected Customers's ID: ", SelectedCustomerID)       
        PaymentMode = request.POST.get('payment_mode')
        print("Payment Mode: ", PaymentMode)
        PaymentAmount = request.POST.get('payment_amount')
        print("Payment Amount: ", PaymentAmount)
        # Save data to Payment Table______________________
        PaymentTable = Payment()
        PaymentTable.payment_mode = PaymentMode
        PaymentTable.payment_amount = PaymentAmount
        PaymentTable.paid_customer_id = Customer.objects.only('customer_id').get(pk=SelectedCustomerID).customer_id
        PaymentTable.paid_cust_name = Customer.objects.only('customer_id').get(pk=SelectedCustomerID).customer_name
        PaymentTable.paid_cust_room_no = Customer.objects.only('customer_id').get(pk=SelectedCustomerID).customer_room_no
        PaymentTable.save()
        messages.success(request, "Payment Info Added Successfully.")
        return redirect('/crud/payment')

    return render(request, 'addPayment.html', context )



def editPayment(request, pk):
    PaymentDetails = Payment.objects.get(payment_id=pk)
    CustomerID = PaymentDetails.paid_customer_id
    print("Customer Code: ",CustomerID)
    if request.method == "POST":
        try:
            # PaymentDetails.payment_date = request.POST.get('payment_date')
            PaymentDetails.payment_amount = request.POST.get('payment_amount')
            PaymentDetails.save()
            messages.success(request, "Customer Updated Successfully")
            return redirect('/crud/payment')
        except:
            messages.error(request, "Enter proper information.")

    context = {'custcode': CustomerID}
    return render(request, 'editPayment.html', context)



def deletePayment(request, pk):
  PaymentDetails = Payment.objects.get(payment_id=pk)
  PaymentDetails.delete()
  messages.error(request, "Record Deleted")
  return redirect('/crud/payment')


def printInvoice(request, pk):
    InvoiceDate = datetime.now().date()
    PaidCustomer_id = Payment.objects.only('paid_customer_id').get(pk=pk).paid_customer_id
    PaidCust_name = Payment.objects.only('paid_customer_id').get(pk=pk).paid_cust_name
    PaidCust_room_no = Payment.objects.only('paid_customer_id').get(pk=pk).paid_cust_room_no
    PaymentMode = Payment.objects.only('paid_customer_id').get(pk=pk).payment_mode
    PaymentAmount = Payment.objects.only('paid_customer_id').get(pk=pk).payment_amount

    context = {
        'invoiceDate' : InvoiceDate,
        'paidCust_id' : PaidCustomer_id,
        'paidCust_name' : PaidCust_name,
        'paidCust_room_no':PaidCust_room_no,
        'paymentMode' : PaymentMode,
        'paymentAmount' : PaymentAmount
    }
    return render(request, 'print.html', context)







'''
obj=Student.objects.filter(Subject.objects.all()).all()
        js=serializers.serialize("json",obj)
'''

