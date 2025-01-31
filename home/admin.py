from django.contrib import admin
from .models import *
from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()
@register.filter
def youtube_video_id(url):
    """Extract YouTube video ID from a URL."""
    try:
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query).get('v', [None])[0]
    except Exception:
        return None

########     ###    ##    ## ##    ## ######## ########  
##     ##   ## ##   ###   ## ###   ## ##       ##     ## 
##     ##  ##   ##  ####  ## ####  ## ##       ##     ## 
########  ##     ## ## ## ## ## ## ## ######   ########  
##     ## ######### ##  #### ##  #### ##       ##   ##   
##     ## ##     ## ##   ### ##   ### ##       ##    ##  
########  ##     ## ##    ## ##    ## ######## ##     ## 
@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image')



 ######  ######## ########  ######## ##    ##  ######   ######## ##     ## 
##    ##    ##    ##     ## ##       ###   ## ##    ##     ##    ##     ## 
##          ##    ##     ## ##       ####  ## ##           ##    ##     ## 
 ######     ##    ########  ######   ## ## ## ##   ####    ##    ######### 
      ##    ##    ##   ##   ##       ##  #### ##    ##     ##    ##     ## 
##    ##    ##    ##    ##  ##       ##   ### ##    ##     ##    ##     ## 
 ######     ##    ##     ## ######## ##    ##  ######      ##    ##     ## 

@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief', 'image', 'id')
    search_fields = ('title', 'brief')  
    list_filter = ('title',)  
    ordering = ('id',)
    fields = ('title', 'brief', 'image')

########  ########   #######  ########  ##     ##  ######  ########     ######     ###    ######## ########  ######    #######  ########  ##    ## 
##     ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##       ##    ##   ## ##      ##    ##       ##    ##  ##     ## ##     ##  ##  ##  
##     ## ##     ## ##     ## ##     ## ##     ## ##          ##       ##        ##   ##     ##    ##       ##        ##     ## ##     ##   ####   
########  ########  ##     ## ##     ## ##     ## ##          ##       ##       ##     ##    ##    ######   ##   #### ##     ## ########     ##    
##        ##   ##   ##     ## ##     ## ##     ## ##          ##       ##       #########    ##    ##       ##    ##  ##     ## ##   ##      ##    
##        ##    ##  ##     ## ##     ## ##     ## ##    ##    ##       ##    ## ##     ##    ##    ##       ##    ##  ##     ## ##    ##     ##    
##        ##     ##  #######  ########   #######   ######     ##        ######  ##     ##    ##    ########  ######    #######  ##     ##    ##    
@admin.register(CategoryLevel1)
class CategoryLevel1Admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CategoryLevel2)
class CategoryLevel2Admin(admin.ModelAdmin):
    list_display = ('name', 'parent')

@admin.register(CategoryLevel3)
class CategoryLevel3Admin(admin.ModelAdmin):
    list_display = ('name', 'parent')


########  ########   #######  ########  ##     ##  ######  ######## 
##     ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##    
##     ## ##     ## ##     ## ##     ## ##     ## ##          ##    
########  ########  ##     ## ##     ## ##     ## ##          ##    
##        ##   ##   ##     ## ##     ## ##     ## ##          ##    
##        ##    ##  ##     ## ##     ## ##     ## ##    ##    ##    
##        ##     ##  #######  ########   #######   ######     ##    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'latest', 'recommend')
    list_filter = ('category', 'latest','recommend')
    search_fields = ('name', 'category__name')


   ###    ########   #######  ##     ## ######## 
  ## ##   ##     ## ##     ## ##     ##    ##    
 ##   ##  ##     ## ##     ## ##     ##    ##    
##     ## ########  ##     ## ##     ##    ##    
######### ##     ## ##     ## ##     ##    ##    
##     ## ##     ## ##     ## ##     ##    ##    
##     ## ########   #######   #######     ##    


@admin.register(AboutUsBanner)
class AboutUsBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(CompanyVoice)
class CompanyVoiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FactoryDetail)
class FactoryDetailAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ChairmanMessage)
class ChairmanMessageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(DirectorMessage)
class DirectorMessageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(VideoSection)
class VideoSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


   ###     ######  ##     ## #### ######## ##     ## ######## ##     ## ######## ##    ## ######## 
  ## ##   ##    ## ##     ##  ##  ##       ##     ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##       ##     ##  ##  ##       ##     ## ##       #### #### ##       ####  ##    ##    
##     ## ##       #########  ##  ######   ##     ## ######   ## ### ## ######   ## ## ##    ##    
######### ##       ##     ##  ##  ##        ##   ##  ##       ##     ## ##       ##  ####    ##    
##     ## ##    ## ##     ##  ##  ##         ## ##   ##       ##     ## ##       ##   ###    ##    
##     ##  ######  ##     ## #### ########    ###    ######## ##     ## ######## ##    ##    ##    


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'alt_text')  # Display fields in the admin list view
    readonly_fields = ('image_preview',)  # Make image preview read-only
    search_fields = ('alt_text',)  # Allow searching by alt text
    ordering = ('id',)  # Order images by ID

    def image_preview(self, obj):
        """Display a preview of the uploaded image in the admin interface."""
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 100px; height: auto;">'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"


########  ########     ###    ##    ##  ######  ##     ## 
##     ## ##     ##   ## ##   ###   ## ##    ## ##     ## 
##     ## ##     ##  ##   ##  ####  ## ##       ##     ## 
########  ########  ##     ## ## ## ## ##       ######### 
##     ## ##   ##   ######### ##  #### ##       ##     ## 
##     ## ##    ##  ##     ## ##   ### ##    ## ##     ## 
########  ##     ## ##     ## ##    ##  ######  ##     ## 

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    search_fields = ('name',)


########  #######   #######  ######## ######## ########  
##       ##     ## ##     ##    ##    ##       ##     ## 
##       ##     ## ##     ##    ##    ##       ##     ## 
######   ##     ## ##     ##    ##    ######   ########  
##       ##     ## ##     ##    ##    ##       ##   ##   
##       ##     ## ##     ##    ##    ##       ##    ##  
##        #######   #######     ##    ######## ##     ## 
@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url') 
    
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'fb_link', 'twitter_link', 'instagram_link', 'youtube_link')
    search_fields = ('title', 'description')
    list_filter = ('fb_link', 'twitter_link', 'instagram_link', 'youtube_link')
    ordering = ('title',)


 ######   #######  ##    ## ########    ###     ######  ########    ##     ##  ######  
##    ## ##     ## ###   ##    ##      ## ##   ##    ##    ##       ##     ## ##    ## 
##       ##     ## ####  ##    ##     ##   ##  ##          ##       ##     ## ##       
##       ##     ## ## ## ##    ##    ##     ## ##          ##       ##     ##  ######  
##       ##     ## ##  ####    ##    ######### ##          ##       ##     ##       ## 
##    ## ##     ## ##   ###    ##    ##     ## ##    ##    ##       ##     ## ##    ## 
 ######   #######  ##    ##    ##    ##     ##  ######     ##        #######   ######  
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'address', 'phone_number')
    
    
   ###    ########  ########   #######  #### ##    ## ##     ## ######## ##    ## ########    
  ## ##   ##     ## ##     ## ##     ##  ##  ###   ## ###   ### ##       ###   ##    ##       
 ##   ##  ##     ## ##     ## ##     ##  ##  ####  ## #### #### ##       ####  ##    ##       
##     ## ########  ########  ##     ##  ##  ## ## ## ## ### ## ######   ## ## ##    ##       
######### ##        ##        ##     ##  ##  ##  #### ##     ## ##       ##  ####    ##       
##     ## ##        ##        ##     ##  ##  ##   ### ##     ## ##       ##   ###    ##       
##     ## ##        ##         #######  #### ##    ## ##     ## ######## ##    ##    ##       

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'calendar', 'phone_number', 'email', 'short_message')
    list_filter = ('calendar',)
    search_fields = ('name', 'phone_number', 'email')
    ordering = ('-calendar',)  # Orders by most recent appointments
    
    
##     ## #### ########  ########  #######      ######   #######  ##    ## ######## ######## ########  ######## ##    ##  ######  ######## 
##     ##  ##  ##     ## ##       ##     ##    ##    ## ##     ## ###   ## ##       ##       ##     ## ##       ###   ## ##    ## ##       
##     ##  ##  ##     ## ##       ##     ##    ##       ##     ## ####  ## ##       ##       ##     ## ##       ####  ## ##       ##       
##     ##  ##  ##     ## ######   ##     ##    ##       ##     ## ## ## ## ######   ######   ########  ######   ## ## ## ##       ######   
 ##   ##   ##  ##     ## ##       ##     ##    ##       ##     ## ##  #### ##       ##       ##   ##   ##       ##  #### ##       ##       
  ## ##    ##  ##     ## ##       ##     ##    ##    ## ##     ## ##   ### ##       ##       ##    ##  ##       ##   ### ##    ## ##       
   ###    #### ########  ########  #######      ######   #######  ##    ## ##       ######## ##     ## ######## ##    ##  ######  ######## 
@admin.register(VideoConference)   
class VideoConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')  # Display these fields in the list view
    search_fields = ('title', 'url')  # Allow searching by title and URL
    list_filter = ('url',)  # Filter by URL if needed


 ######   #######  ##    ## ########    ###     ######  ########    ########  #######  ########  ##     ## 
##    ## ##     ## ###   ##    ##      ## ##   ##    ##    ##       ##       ##     ## ##     ## ###   ### 
##       ##     ## ####  ##    ##     ##   ##  ##          ##       ##       ##     ## ##     ## #### #### 
##       ##     ## ## ## ##    ##    ##     ## ##          ##       ######   ##     ## ########  ## ### ## 
##       ##     ## ##  ####    ##    ######### ##          ##       ##       ##     ## ##   ##   ##     ## 
##    ## ##     ## ##   ###    ##    ##     ## ##    ##    ##       ##       ##     ## ##    ##  ##     ## 
 ######   #######  ##    ##    ##    ##     ##  ######     ##       ##        #######  ##     ## ##     ## 

@admin.register(CompanyInquiry)
class CompanyInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'email', 'location', 'created_at')
    search_fields = ('name', 'phone_no', 'email', 'location')
