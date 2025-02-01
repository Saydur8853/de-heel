from django.core.validators import RegexValidator
from django.db import models
import re
from bs4 import BeautifulSoup
from colorfield.fields import ColorField


YOUTUBE_REGEX = r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'


########     ###    ##    ## ##    ## ######## ########  
##     ##   ## ##   ###   ## ###   ## ##       ##     ## 
##     ##  ##   ##  ####  ## ####  ## ##       ##     ## 
########  ##     ## ## ## ## ## ## ## ######   ########  
##     ## ######### ##  #### ##  #### ##       ##   ##   
##     ## ##     ## ##   ### ##   ### ##       ##    ##  
########  ##     ## ##    ## ##    ## ######## ##     ## 
# Create your models here.
class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name="Banner Image")
    title = models.CharField(max_length=200, verbose_name="Banner Title")
    subtitle = models.TextField(blank=True, verbose_name="Banner Subtitle")

    def __str__(self):
        return self.title

 ######  ######## ########  ######## ##    ##  ######   ######## ##     ## 
##    ##    ##    ##     ## ##       ###   ## ##    ##     ##    ##     ## 
##          ##    ##     ## ##       ####  ## ##           ##    ##     ## 
 ######     ##    ########  ######   ## ## ## ##   ####    ##    ######### 
      ##    ##    ##   ##   ##       ##  #### ##    ##     ##    ##     ## 
##    ##    ##    ##    ##  ##       ##   ### ##    ##     ##    ##     ## 
 ######     ##    ##     ## ######## ##    ##  ######      ##    ##     ## 

class Strength(models.Model):
    title = models.CharField(max_length=100)
    brief = models.TextField()
    image = models.ImageField(upload_to='strength_images/')
    
    def __str__(self):
        return self.title


########  ########   #######  ########  ##     ##  ######  ########     ######     ###    ######## ########  ######    #######  ########  ##    ## 
##     ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##       ##    ##   ## ##      ##    ##       ##    ##  ##     ## ##     ##  ##  ##  
##     ## ##     ## ##     ## ##     ## ##     ## ##          ##       ##        ##   ##     ##    ##       ##        ##     ## ##     ##   ####   
########  ########  ##     ## ##     ## ##     ## ##          ##       ##       ##     ##    ##    ######   ##   #### ##     ## ########     ##    
##        ##   ##   ##     ## ##     ## ##     ## ##          ##       ##       #########    ##    ##       ##    ##  ##     ## ##   ##      ##    
##        ##    ##  ##     ## ##     ## ##     ## ##    ##    ##       ##    ## ##     ##    ##    ##       ##    ##  ##     ## ##    ##     ##    
##        ##     ##  #######  ########   #######   ######     ##        ######  ##     ##    ##    ########  ######    #######  ##     ##    ##    
class CategoryLevel1(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Level 1")

    def __str__(self):
        return self.name


class CategoryLevel2(models.Model):
    parent = models.ForeignKey(CategoryLevel1, on_delete=models.CASCADE, related_name='level2_categories', verbose_name="Parent Category (Level 1)")
    name = models.CharField(max_length=100, verbose_name="Category Level 2")
    image = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image")

    def __str__(self):
        return f"{self.parent} -> {self.name}"


class CategoryLevel3(models.Model):
    parent = models.ForeignKey(CategoryLevel2, on_delete=models.CASCADE, related_name='level3_categories', verbose_name="Parent Category (Level 2)")
    name = models.CharField(max_length=100, verbose_name="Category Level 3")

    def __str__(self):
        return f"{self.parent} -> {self.name}"


########  ########   #######  ########  ##     ##  ######  ######## 
##     ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##    
##     ## ##     ## ##     ## ##     ## ##     ## ##          ##    
########  ########  ##     ## ##     ## ##     ## ##          ##    
##        ##   ##   ##     ## ##     ## ##     ## ##          ##    
##        ##    ##  ##     ## ##     ## ##     ## ##    ##    ##    
##        ##     ##  #######  ########   #######   ######     ##    

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name="Product Price")
    image = models.ImageField(upload_to='products/', verbose_name="Product Image")
    category = models.ForeignKey('CategoryLevel3', on_delete=models.CASCADE, related_name='products', verbose_name="Category")
    stock = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="Stock Quantity")
    latest = models.BooleanField(default=False, verbose_name="Latest Product")
    minimum_order_quantity = models.PositiveIntegerField(blank=True, null=True)
    
    # Color fields
    color_1 = ColorField(verbose_name="Product Color 1", blank=True, null=True, help_text="Enter color hex code (e.g., #FFFFFF)")
    color_2 = ColorField(verbose_name="Product Color 2", blank=True, null=True, help_text="Enter color hex code (e.g., #FFFFFF)")
    color_3 = ColorField(verbose_name="Product Color 3", blank=True, null=True, help_text="Enter color hex code (e.g., #FFFFFF)")
    color_4 = ColorField(verbose_name="Product Color 4", blank=True, null=True, help_text="Enter color hex code (e.g., #FFFFFF)")
    color_5 = ColorField(verbose_name="Product Color 5", blank=True, null=True, help_text="Enter color hex code (e.g., #FFFFFF)")


    # Size fields
    size_1 = models.CharField(max_length=20, verbose_name="Product Size 1", blank=True, null=True)
    size_2 = models.CharField(max_length=20, verbose_name="Product Size 2", blank=True, null=True)
    size_3 = models.CharField(max_length=20, verbose_name="Product Size 3", blank=True, null=True)
    size_4 = models.CharField(max_length=20, verbose_name="Product Size 4", blank=True, null=True)
    size_5 = models.CharField(max_length=20, verbose_name="Product Size 5", blank=True, null=True)
    
    # Additional image fields
    image_1 = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image 1")
    image_2 = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image 2")
    image_3 = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image 3")
    image_4 = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image 4")
    image_5 = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name="Product Image 5")
    
    recommend = models.BooleanField(default=False, verbose_name="Want to recommend? ")

    def __str__(self):
        return self.name



   ###    ########   #######  ##     ## ######## 
  ## ##   ##     ## ##     ## ##     ##    ##    
 ##   ##  ##     ## ##     ## ##     ##    ##    
##     ## ########  ##     ## ##     ##    ##    
######### ##     ## ##     ## ##     ##    ##    
##     ## ##     ## ##     ## ##     ##    ##    
##     ## ########   #######   #######     ##    


class AboutUs(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return "About Us Section"
    

class AboutUsBanner(models.Model):
    image = models.ImageField(upload_to='about_us/banner/', verbose_name="Banner Image")
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Title (Optional)")
    subtitle = models.TextField(blank=True, null=True, verbose_name="Subtitle")

    def __str__(self):
        return self.title if self.title else "About Us Banner"


class CompanyVoice(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.title


class FactoryDetail(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    image = models.ImageField(upload_to='about_us/factory/', verbose_name="Factory Image")

    def __str__(self):
        return self.title


class ChairmanMessage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    image = models.ImageField(upload_to='about_us/chairman/', verbose_name="Chairman Image")

    def __str__(self):
        return self.title

class DirectorMessage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    image = models.ImageField(upload_to='about_us/director/', verbose_name="Director Image")

    def __str__(self):
        return self.title


class VideoSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", blank=True, null=True)
    video_link = models.URLField(blank=True, null=True, verbose_name="Video Link")
    video_file = models.FileField(upload_to='about_us/videos/', blank=True, null=True, verbose_name="Video File")
    background_image = models.ImageField(upload_to='about_us/backgrounds/', blank=True, null=True, verbose_name="Background Image")

    @property
    def embed_url(self):
        """Extract video ID and construct embed URL."""
        if self.video_link:
            match = re.search(r'(?:v=|\/embed\/|\/watch\?v=|\/)([a-zA-Z0-9_-]{11})', self.video_link)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/embed/{video_id}"
        return None

    def __str__(self):
        return self.title if self.title else "Video Section"


class TeamMember(models.Model):
    image = models.ImageField(upload_to='our_team/', verbose_name="Member Image")
    name = models.CharField(max_length=200, verbose_name="Member Name")
    designation = models.CharField(max_length=200, verbose_name="Designation")

    def __str__(self):
        return self.name

class MissionVision(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", blank=True, null=True)
    image = models.ImageField(upload_to='mission_vision/', verbose_name="Image")
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.title

class ImageGallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Gallery Image")
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Title (Optional)")
    caption = models.TextField(blank=True, null=True, verbose_name="Caption (Optional)")

    def __str__(self):
        return self.title or f"Image {self.id}"


   ###     ######  ##     ## #### ######## ##     ## ######## ##     ## ######## ##    ## ######## 
  ## ##   ##    ## ##     ##  ##  ##       ##     ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##       ##     ##  ##  ##       ##     ## ##       #### #### ##       ####  ##    ##    
##     ## ##       #########  ##  ######   ##     ## ######   ## ### ## ######   ## ## ##    ##    
######### ##       ##     ##  ##  ##        ##   ##  ##       ##     ## ##       ##  ####    ##    
##     ## ##    ## ##     ##  ##  ##         ## ##   ##       ##     ## ##       ##   ###    ##    
##     ##  ######  ##     ## #### ########    ###    ######## ##     ## ######## ##    ##    ##    

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/', verbose_name="Carousel Image")
    alt_text = models.CharField(max_length=255, verbose_name="Alt Text", blank=True)

    def __str__(self):
        return self.alt_text or f"Carousel Image {self.id}"

########  ########     ###    ##    ##  ######  ##     ## 
##     ## ##     ##   ## ##   ###   ## ##    ## ##     ## 
##     ## ##     ##  ##   ##  ####  ## ##       ##     ## 
########  ########  ##     ## ## ## ## ##       ######### 
##     ## ##   ##   ######### ##  #### ##       ##     ## 
##     ## ##    ##  ##     ## ##   ### ##    ## ##     ## 
########  ##     ## ##     ## ##    ##  ######  ##     ## 

class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Branch Name")
    image = models.ImageField(upload_to='branches/', verbose_name="Branch Image")
    description = models.TextField(blank=True, verbose_name="Branch Description")

    def __str__(self):
        return self.name


########  #######   #######  ######## ######## ########  
##       ##     ## ##     ##    ##    ##       ##     ## 
##       ##     ## ##     ##    ##    ##       ##     ## 
######   ##     ## ##     ##    ##    ######   ########  
##       ##     ## ##     ##    ##    ##       ##   ##   
##       ##     ## ##     ##    ##    ##       ##    ##  
##        #######   #######     ##    ######## ##     ## 
class FooterLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self):
        return self.name

class Footer(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name="Site logo")
    title = models.CharField(max_length=100)
    description = models.TextField()
    fb_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
    
 ######   #######  ##    ## ######## ##     ##  ######  ########    ##     ##  ######  
##    ## ##     ## ###   ##    ##    ##     ## ##    ##    ##       ##     ## ##    ## 
##       ##     ## ####  ##    ##    ##     ## ##          ##       ##     ## ##       
##       ##     ## ## ## ##    ##    ##     ## ##          ##       ##     ##  ######  
##       ##     ## ##  ####    ##    ##     ## ##          ##       ##     ##       ## 
##    ## ##     ## ##   ###    ##    ##     ## ##    ##    ##       ##     ## ##    ## 
 ######   #######  ##    ##    ##     #######   ######     ##        #######   ######  
 
class ContactUs(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100, verbose_name="Title")
    phone_number = models.CharField(blank=True, null=True, max_length=25, verbose_name="Phone Number")
    company_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="Company Name") 
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    api_key = models.CharField(max_length=255, verbose_name="Google Maps API Key", blank=True, null=True)
    embed_code = models.CharField(max_length=1000, verbose_name="Embed Code", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.embed_code:
            # Parse the embed code to extract the src attribute
            soup = BeautifulSoup(self.embed_code, 'html.parser')
            iframe = soup.find('iframe')
            if iframe and iframe.get('src'):
                self.embed_code = iframe['src']  # Save only the src attribute
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title or self.company_name

    
   ###    ########  ########   #######  #### ##    ## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##     ##  ##  ###   ## ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##     ##  ##  ####  ## #### #### ##       ####  ##    ##    
##     ## ########  ########  ##     ##  ##  ## ## ## ## ### ## ######   ## ## ##    ##    
######### ##        ##        ##     ##  ##  ##  #### ##     ## ##       ##  ####    ##    
##     ## ##        ##        ##     ##  ##  ##   ### ##     ## ##       ##   ###    ##    
##     ## ##        ##         #######  #### ##    ## ##     ## ######## ##    ##    ##    

class Appointment(models.Model):
    calendar = models.DateTimeField(verbose_name="Appointment Date and Time")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    short_message = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
    

##     ## #### ########  ########  #######      ######   #######  ##    ## ######## ######## ########  ######## ##    ##  ######  ######## 
##     ##  ##  ##     ## ##       ##     ##    ##    ## ##     ## ###   ## ##       ##       ##     ## ##       ###   ## ##    ## ##       
##     ##  ##  ##     ## ##       ##     ##    ##       ##     ## ####  ## ##       ##       ##     ## ##       ####  ## ##       ##       
##     ##  ##  ##     ## ######   ##     ##    ##       ##     ## ## ## ## ######   ######   ########  ######   ## ## ## ##       ######   
 ##   ##   ##  ##     ## ##       ##     ##    ##       ##     ## ##  #### ##       ##       ##   ##   ##       ##  #### ##       ##       
  ## ##    ##  ##     ## ##       ##     ##    ##    ## ##     ## ##   ### ##       ##       ##    ##  ##       ##   ### ##    ## ##       
   ###    #### ########  ########  #######      ######   #######  ##    ## ##       ######## ##     ## ######## ##    ##  ######  ######## 
class VideoConference(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title
    
 ######   #######  ##    ## ########    ###     ######  ########    ########  #######  ########  ##     ## 
##    ## ##     ## ###   ##    ##      ## ##   ##    ##    ##       ##       ##     ## ##     ## ###   ### 
##       ##     ## ####  ##    ##     ##   ##  ##          ##       ##       ##     ## ##     ## #### #### 
##       ##     ## ## ## ##    ##    ##     ## ##          ##       ######   ##     ## ########  ## ### ## 
##       ##     ## ##  ####    ##    ######### ##          ##       ##       ##     ## ##   ##   ##     ## 
##    ## ##     ## ##   ###    ##    ##     ## ##    ##    ##       ##       ##     ## ##    ##  ##     ## 
 ######   #######  ##    ##    ##    ##     ##  ######     ##       ##        #######  ##     ## ##     ## 
 
class CompanyInquiry(models.Model):
    name = models.CharField(max_length=100)  # New field for name
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"
