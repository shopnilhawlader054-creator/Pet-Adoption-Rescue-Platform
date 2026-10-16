from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from core.models import Pet,Adoptions
from django.contrib import messages
from .froms import Registationform,Adoptionform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def home (request):
    print('hitting sucess')
    pets =  Pet.objects.all()
    context ={
        'pets':pets,
    }
    return render(request,'home.html',context)
@login_required
def pet_detal (request,pk):
    print('pet detals hitting sucess')
    pets = get_object_or_404 (Pet, id=pk)
    print(pets.name)
    context ={
        'pet':pets,
    }
    return render(request,'pet_detail.html',context)
@login_required
def application_form(request,pk):
    user_id = get_object_or_404(Pet,id=pk)
    if request.method == 'POST':
        adoption = Adoptionform(request.POST)
        if adoption.is_valid():
            adoption_instance = adoption.save(commit=False)
            adoption_instance.pet = user_id
            adoption_instance.user = request.user
            adoption.save()
            return redirect('home')
        else:
            print("FORM ERRORS:", adoption.errors)
        
    print('application form')
    pets = get_object_or_404(Pet,id=pk)
    context ={
        'pet':pets
    }
    return render(request,'adoption_form.html',context)

def filterpet(request):
    pet_name = request.GET.get('petname')
    pet_type = request.GET.get('type')
    gender = request.GET.get('gender')
    location = request.GET.get('location')
    pet = Pet.objects.all()
    
    if pet_name:
            pet = pet.filter(name__iexact =pet_name)
    if pet_type:
            pet = pet.filter(animal_type__iexact =pet_type)
    if gender :
            pet = pet.filter(gender__iexact=gender)
    if location:
            pet = pet.filter(location__iexact=location)
    context = {
        "pets":pet
    }
    return render(request,'home.html',context)
@login_required
def dashbord(request):
    user = request.user
    adoptions = Adoptions.objects.filter(user=request.user)
    user_name = user.username
    print(user_name)
    context = {
        'username':user_name,
        'adoptions':adoptions
    }
    for adoption in adoptions:
          print(adoption)

    return render(request,'dashbord.html',context)
def logins(request):
    if request.method =='POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        print("INPUT USERNAME:", user_name)
        print("INPUT PASSWORD:", pass_word)
        user = authenticate (request,username = user_name,password = pass_word)
        if user is not None:
            print('user in')
            login(request,user)
            messages.success(request,"Successfully Logged In!")
            return redirect ('dashbord')
        else:
            messages.error(request,'login failed')
            return redirect('login')
    
            
    print('application form')
    return render(request,'login.html')

def logouts(request):
    logout(request)
    print('log out sucess')
    return redirect('login')
def register(request):
    if request.method == 'POST':
         print('hitting sucess')
         register_form = Registationform(request.POST)
         if register_form.is_valid():
             print('hitting sucess')
             register_form.save()
             messages.success(request,'registed sucessfull')
             return redirect('login')
         else:
            print("FORM ERRORS:", register_form.errors)
            messages.error(request,'registed fail')
    else:
        register_form = Registationform()
    
    return render(request,'register.html',{'context':register_form})
# def register(request):
#     if request.method == 'POST':
#         register_form = Registationform(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             return redirect('login')

    
#     # এটি ফাংশনের একদম সোজা লাইনে (বাইরে) থাকবে, 
#     # যাতে GET রিকোয়েস্ট হোক বা ফর্ম ইনভ্যালিড হোক—সবসময় পেজটি রেন্ডার হয়ে রেসপন্স চলে যায়!
#     return render(request, 'register.html')