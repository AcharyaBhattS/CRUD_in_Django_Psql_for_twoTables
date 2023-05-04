from django.shortcuts import render

# Create your views here.
# Display Customer Data
def home(request):
    return render(request, 'home.html')