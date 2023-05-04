from django.shortcuts import render, redirect
from .models import Customer, Invoice
from django.contrib import messages
from datetime import datetime
import os


# Display Customer Data
def home(request):
    return render(request, 'home.html')

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
        CustName = request.POST.get('cust_name')
        print("CustName: ", CustName)
        customer_room_no = request.POST.get('cust_room_no')
        print("customer_room_no: ", customer_room_no)
        Check_In_Date = request.POST.get('check_in_dt')
        print("Check-In Date: ", Check_In_Date)
        Check_Out_Date = request.POST.get('check_out_dt')
        print("Check-Out Date: ", Check_Out_Date)
        try:
            custTableData.customer_name = CustName
            custTableData.room_no = customer_room_no
            custTableData.checkin_date = Check_In_Date
            custTableData.checkout_date = Check_Out_Date
            custTableData.save()
            messages.success(request, "Customer Added Successfully.")
            return redirect('/customer')
        except:
            messages.error(request, "Enter proper information.")
    return render(request, 'addCustomer.html')



def editCust(request, pk):
    custTableData = Customer.objects.get(customer_id=pk)
    if request.method == "POST":
        try:
            custTableData.customer_name = request.POST.get('cust_name')
            custTableData.room_no = request.POST.get('cust_room_no')
            custTableData.checkin_date = request.POST.get('check_in_dt')
            custTableData.checkout_date = request.POST.get('check_out_dt')
            custTableData.save()
            messages.success(request, "Customer Updated Successfully")
            return redirect('/customer')
        except:
            messages.error(request, "Enter proper information.")

    context = {'cust':custTableData}
    return render(request, 'editCustomer.html', context)


def deleteCust(request, pk):
  custTableData = Customer.objects.get(customer_id=pk)
  custTableData.delete()
  messages.error(request, "Record Deleted")
  return redirect('/customer')



#__Payment___________________________________________________________________PAYMENT____
# Display Payment Data
def showPayment(request):
    InvoiceTable = Invoice.objects.all()
    context = {'pay_details':InvoiceTable}
    return render(request, 'invoiceTable.html', context)



# # Insert Payment Data
def addPayment(request):
    customerDetails = Customer.objects.all()
    context = {'cust_details':customerDetails}
    
    if request.method == "POST":
        SelectedCustomerID = request.POST.get('selectcustomer')
        print("\nSelected Customers's ID: ", SelectedCustomerID)
        InvoiceDate =  request.POST.get('bill_date')
        PaidAmount = request.POST.get('payment_amount')
        print("Payment Amount: ", PaidAmount)
        # Save data to Payment Table______________________
        PaymentTable = Invoice()
        PaymentTable.customer_id = Customer.objects.only('customer_id').get(pk=SelectedCustomerID).customer_id
        PaymentTable.customer_name = Customer.objects.only('customer_id').get(pk=SelectedCustomerID).customer_name
        PaymentTable.bill_date = InvoiceDate
        PaymentTable.amount_paid = PaidAmount
        PaymentTable.save()
        messages.success(request, "Payment Info Added Successfully.")
        return redirect('/payment')

    return render(request, 'addPayment.html', context )



def editPayment(request, pk):
    PaymentDetails = Invoice.objects.get(payment_id=pk)
    CustomerID = PaymentDetails.paid_customer_id
    print("Customer Code: ",CustomerID)
    if request.method == "POST":
        try:
            # PaymentDetails.payment_date = request.POST.get('payment_date')
            PaymentDetails.payment_amount = request.POST.get('payment_amount')
            PaymentDetails.save()
            messages.success(request, "Customer Updated Successfully")
            return redirect('/payment')
        except:
            messages.error(request, "Enter proper information.")

    context = {'custcode': CustomerID}
    return render(request, 'editPayment.html', context)



def deletePayment(request, pk):
  PaymentDetails = Invoice.objects.get(payment_id=pk)
  PaymentDetails.delete()
  messages.error(request, "Record Deleted")
  return redirect('/crud/payment')




