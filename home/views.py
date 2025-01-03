from django.shortcuts import render
from .models import *

def home(request):
    banner = BannerModel.objects.last()
    strengths = Strength.objects.all()
    carousel_images = CarouselImage.objects.all()
    branches = Branch.objects.all() 
    gallery_images = ImageGallery.objects.all()
    video_section = VideoSection.objects.last()

    category_level1_list = CategoryLevel1.objects.prefetch_related('level2_categories').all()
    latest_products = Product.objects.filter(latest=True)
    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 
    
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
        'footer_links': footer_links
   
    }
    
    return render(request, 'home.html', context)



def about(request):
    banner = AboutUsBanner.objects.last()
    company_voice = CompanyVoice.objects.last()
    factory_detail = FactoryDetail.objects.last()
    video_section = VideoSection.objects.first()
    chairman_message = ChairmanMessage.objects.last()
    director_message = DirectorMessage.objects.last()
    team_members = TeamMember.objects.all()
    mission_vision = MissionVision.objects.all()
    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 
    
    context = {
        "banner": banner,
        "company_voice": company_voice,
        "factory_detail": factory_detail,
        "video_section": video_section,
        "chairman_message": chairman_message,
        "director_message": director_message,
        "team_members": team_members,
        "mission_vision": mission_vision,
        'footer': footer,
        'footer_links': footer_links
   
        
    }
    return render(request, 'about.html', context)


def product(request):
    level1_categories = CategoryLevel1.objects.prefetch_related('level2_categories__level3_categories')
    category_level1 = request.GET.get('category_level1')
    category_level2 = request.GET.get('category_level2')
    category_level3 = request.GET.get('category_level3')
    category_all = request.GET.get('category')

    footer = Footer.objects.first()
    footer_links = FooterLink.objects.all() 

    products = Product.objects.order_by('-id')

    if category_all == "all":
        pass
    elif category_level3:
        products = products.filter(category_id=category_level3)
    elif category_level2:
        products = products.filter(category__parent_id=category_level2)
    elif category_level1:
        products = products.filter(category__parent__parent_id=category_level1)

    context = {
        'level1_categories': level1_categories,
        'products': products,
        'footer': footer,
        'footer_links': footer_links
   
    }
    return render(request, 'products.html', context)
