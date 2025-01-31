from django.utils import timezone
from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator

def home(request):
    banner = BannerModel.objects.last()
    strengths = Strength.objects.all()
    carousel_images = CarouselImage.objects.all()
    branches = Branch.objects.all() 
    gallery_images = ImageGallery.objects.all()
    video_section = VideoSection.objects.last()
    
    level1_categories = CategoryLevel1.objects.prefetch_related('level2_categories__level3_categories')
    products = Product.objects.order_by('-id')
    category_level1 = request.GET.get('category_level1')
    category_level2 = request.GET.get('category_level2')
    category_level3 = request.GET.get('category_level3')
    category_all = request.GET.get('category')
    
    if category_all == "all":
        pass
    elif category_level3:
        products = products.filter(category_id=category_level3)
    elif category_level2:
        products = products.filter(category__parent_id=category_level2)
    elif category_level1:
        products = products.filter(category__parent__parent_id=category_level1)
        
    

    category_level1_list = CategoryLevel1.objects.prefetch_related('level2_categories').all()
    latest_products = Product.objects.filter(latest=True)
    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 
    contact_us = ContactUs.objects.first()
    new_appointments = Appointment.objects.filter(viewed=False).order_by('-calendar')[:5]
    has_new_appointments = new_appointments.exists()
    video_conferences = VideoConference.objects.all()
    
    context = {
        'banner': banner,
        'carousel_images': carousel_images,
        'branches': branches,
        'gallery_images': gallery_images,
        'video_section': video_section,
        'strengths': strengths,
        "category_level1_list": category_level1_list,
        'latest_products': latest_products,
        'footer': footer,
        'footer_links': footer_links,
        'contact_us': contact_us,
        'new_appointments': new_appointments,
        'has_new_appointments': has_new_appointments,
        'video_conferences': video_conferences,
        'level1_categories': level1_categories,
        'products': products,
   
    }
    
    return render(request, 'home.html', context)

def submit_appointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        calendar = request.POST.get('calendar')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email', '')
        short_message = request.POST.get('short_message')

        # Convert the string calendar value to a datetime object
        try:
            calendar = timezone.make_aware(datetime.strptime(calendar, '%Y-%m-%dT%H:%M'))
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect('home')  # Redirect if the date format is invalid

        # Check if the appointment date is in the past
        if calendar < timezone.now():
            messages.error(request, "Appointment date cannot be in the past.")
            return redirect('home')  # Redirect to the home page or another page

        if name and calendar and phone_number:  # Basic validation
            Appointment.objects.create(
                name=name,
                calendar=calendar,
                phone_number=phone_number,
                email=email,
                short_message=short_message
            )
            messages.success(request, "Your appointment request has been submitted.")
        else:
            messages.error(request, "Please fill in all required fields.")

        return redirect('home')  # Redirect to the home page or another page

    return redirect('home')

@csrf_exempt
def mark_appointment_as_viewed(request, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.viewed = True  # Use the `viewed` field
            appointment.save()
            return JsonResponse({'status': 'success'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def submit_company_inquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        location = request.POST.get('location')

        # Basic validation
        if name and phone_no and email and location:
            # Save the inquiry
            CompanyInquiry.objects.create(
                name=name,
                phone_no=phone_no,
                email=email,
                location=location
            )
            messages.success(request, "Your company inquiry has been submitted.")
        else:
            messages.error(request, "Please fill in all required fields.")

        return redirect('home')  # Redirect to the home page or another page

    return redirect('home')

def about(request):
    banner = AboutUsBanner.objects.last()
    company_voice = CompanyVoice.objects.last()
    factory_detail = FactoryDetail.objects.last()
    video_section = VideoSection.objects.first()
    contact_us = ContactUs.objects.first()
    chairman_message = ChairmanMessage.objects.last()
    director_message = DirectorMessage.objects.last()
    team_members = TeamMember.objects.all()
    mission_vision = MissionVision.objects.all()
    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 
    
    
    level1_categories = CategoryLevel1.objects.prefetch_related('level2_categories__level3_categories')
    products = Product.objects.order_by('-id')
    category_level1 = request.GET.get('category_level1')
    category_level2 = request.GET.get('category_level2')
    category_level3 = request.GET.get('category_level3')
    category_all = request.GET.get('category')
    video_conferences = VideoConference.objects.all()
    
    if category_all == "all":
        pass
    elif category_level3:
        products = products.filter(category_id=category_level3)
    elif category_level2:
        products = products.filter(category__parent_id=category_level2)
    elif category_level1:
        products = products.filter(category__parent__parent_id=category_level1)
    
    context = {
        "banner": banner,
        "company_voice": company_voice,
        "factory_detail": factory_detail,
        "video_section": video_section,
        'contact_us': contact_us,
        "chairman_message": chairman_message,
        "director_message": director_message,
        "team_members": team_members,
        "mission_vision": mission_vision,
        'footer': footer,
        'footer_links': footer_links,
        'level1_categories': level1_categories,
        'products': products,
        'video_conferences': video_conferences,
    }
    return render(request, 'about.html', context)


from django.core.paginator import Paginator

def product(request):
    level1_categories = CategoryLevel1.objects.prefetch_related('level2_categories__level3_categories')
    category_level1 = request.GET.get('category_level1')
    category_level2 = request.GET.get('category_level2')
    category_level3 = request.GET.get('category_level3')
    category_all = request.GET.get('category')

    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all()
    contact_us = ContactUs.objects.first()

    # Start by getting all products
    products = Product.objects.all()

    # Apply filtering based on category level
    if category_all == "all":
        pass
    elif category_level3:
        # Filter by level 3 category
        products = products.filter(category_id=category_level3)
    elif category_level2:
        # Filter by level 2 category
        products = products.filter(category__parent_id=category_level2)
    elif category_level1:
        # Filter by level 1 category
        products = products.filter(category__parent__parent_id=category_level1)

    # Pagination
    paginator = Paginator(products, 25)  # Show 30 products per page
    page_number = request.GET.get('page')  # Get the current page number from the URL query params
    page_obj = paginator.get_page(page_number)
    video_conferences = VideoConference.objects.all()

    context = {
        'level1_categories': level1_categories,
        'products': page_obj,  # Pass the page object to the template
        'footer': footer,
        'footer_links': footer_links,
        'contact_us': contact_us,
        'video_conferences': video_conferences,
    }

    return render(request, 'products.html', context)


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 
    contact_us = ContactUs.objects.first()
    
    recommended_products = Product.objects.filter(recommend=True).exclude(id=product.id)[:4]
    video_conferences = VideoConference.objects.all()
    
    context = {
        'product': product,
        'footer': footer,
        'footer_links': footer_links,
        'contact_us': contact_us,
        'recommended_products': recommended_products,
        'video_conferences': video_conferences,
      
    }
    return render(request, 'product-details.html', context)


