from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print("✅ User is logged in:", request.user)
    else:
        print("❌ User is not logged in")
    return render(request,"homepage/mainpage.html")


