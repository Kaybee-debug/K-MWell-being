from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Application
from .forms import ApplicationForm
# Create your views here.

# def listing_list(request):
#     listings = Listing.objects.all()
#     context = {
#         "listings": listings
#     }
#     return render(request, "listings.html", context)

# def listing_retrieve(request, pk):
#     listing = Listing.objects.get(id=pk)
#     context = {
#         "listing": listing
#     }
#     return render(request, "listing.html", context)



def member_create(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()  # <-- this will create a new listing
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "member_create.html", context)

# def listing_update(request, pk):
#     listing = Listing.objects.get(id=pk)
#     form = ListingForm(instance=listing)
#     if request.method == "POST":
#         form = ListingForm(request.POST,instance=listing,files=request.FILES)
#         if form.is_valid():
#             form.save()  # <-- this will create a new listing
#             return redirect("/")
#     context = {
#         "form": form
#     }
#     return render(request, "update.html", context)

# def listing_delete(request, pk):
#     listing = Listing.objects.get(id=pk)
#     listing.delete()
#     redirect("/")

# # Create your views here.
# def member(request):
#     return render(request,'member.html')
