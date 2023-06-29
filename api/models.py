from django.db import models

# Create your models here.


class Header_section(models.Model):
    PageType = models.CharField(max_length=100, blank=True, null=True) 
    header_h1_content = models.TextField(max_length=225, blank=True, null=True)
    header_p_content = models.TextField(max_length=225, blank=True, null=True)
    header_image = models.FileField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.PageType)

class Home_client_section(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    img = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Home (Client Section)"

    def __str__(self) -> str:
        return str(self.title)

class Home_overwhelmed_section(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    img1 = models.FileField(blank=True, null=True)
    content1 = models.TextField(max_length=225, blank=True, null=True)
    img2 = models.FileField(blank=True, null=True)
    content2 = models.TextField(max_length=225, blank=True, null=True)
    img3 = models.FileField(blank=True, null=True)
    content3 = models.TextField(max_length=225, blank=True, null=True)
    img4 = models.FileField(blank=True, null=True)
    content4 = models.TextField(max_length=225, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Home (Feeling Overwhelmed Section)"

    def __str__(self) -> str:
        return str(self.title)

class Home_proposal_section(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    paragraph1 = models.TextField(max_length=225, blank=True, null=True)
    paragraph2 = models.TextField(max_length=225, blank=True, null=True)
    paragraph3 = models.TextField(max_length=225, blank=True, null=True)
    paragraph4 = models.TextField(max_length=225, blank=True, null=True)
    image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Home (Proposal Section)"

    def __str__(self) -> str:
        return str(self.title)

class Home_service_section(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    icon = models.FileField(null=True, blank=True)
    content = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Home (Service Section)"

    def __str__(self) -> str:
        return str(self.title)

class Home_step_process_section(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text_header = models.CharField(max_length=100, blank=True, null=True)
    step1 = models.CharField(max_length=100, blank=True, null=True)
    content1 = models.CharField(max_length=200, blank=True, null=True)
    step2 = models.CharField(max_length=100, blank=True, null=True)
    content2 = models.CharField(max_length=200, blank=True, null=True)
    step3 = models.CharField(max_length=100, blank=True, null=True)
    content3 = models.CharField(max_length=200, blank=True, null=True)
    content4 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Home (3 Step Process Section)"

    def __str__(self) -> str:
        return str(self.title)

class Home_happy_customer(models.Model):
    customer_image = models.FileField(blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_comment = models.TextField(max_length=225, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Happy Customer Section"

    def __str__(self) -> str:
        return str(self.customer_name)
    
class About_Us(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    who_is_amorserv_content = models.TextField(max_length=500, null=True, blank=True)
    vision_image1 = models.FileField(null=True, blank=True)
    vision_title1 = models.CharField(max_length=50, null=True, blank=True)
    vision_content1 = models.TextField(max_length=200, null=True, blank=True)
    vision_image2 = models.FileField(null=True, blank=True)
    vision_title2 = models.CharField(max_length=50, null=True, blank=True)
    vision_content2 = models.TextField(max_length=200, null=True, blank=True)
    vision_image3 = models.FileField(null=True, blank=True)
    vision_title3 = models.CharField(max_length=50, null=True, blank=True)
    vision_content3 = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self) -> str:
        return str(self.title)
    

class About_team(models.Model):
    team_member_name = models.CharField(max_length=50, null=True, blank=True)
    team_member_role = models.CharField(max_length=50, null=True, blank=True)
    team_member_image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "About (Team Members Section)"

    def __str__(self) -> str:
        return str(self.team_member_name)
    
class About_partner(models.Model):
    partner_name = models.CharField(max_length=50, null=True, blank=True)
    partner_image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "About (Partners Section)"

    def __str__(self) -> str:
        return str(self.partner_name)

class Portfolio(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    paragraph1_content = models.TextField(max_length=500, null=True, blank=True)
    paragraph2_content = models.TextField(max_length=500, null=True, blank=True)
    paragraph3_content = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.company_name)

class Service(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)
    header_text = models.CharField(max_length=100, null=True, blank=True)
    service_section1_header = models.CharField(max_length=50, null=True, blank=True)
    service_section1_content = models.TextField(max_length=500, null=True, blank=True)
    service_section1_image = models.FileField(null=True, blank=True)
    service_section2_header = models.CharField(max_length=50, null=True, blank=True)
    service_section2_content = models.TextField(max_length=500, null=True, blank=True)
    service_section2_image = models.FileField(null=True, blank=True)
    service_section3_header = models.CharField(max_length=50, null=True, blank=True)
    service_section3_content = models.TextField(max_length=500, null=True, blank=True)
    service_section3_image = models.FileField(null=True, blank=True)
    service_section4_header = models.CharField(max_length=50, null=True, blank=True)
    service_section4_content = models.TextField(max_length=500, null=True, blank=True)
    service_section4_image = models.FileField(null=True, blank=True)
    service_section5_header = models.CharField(max_length=50, null=True, blank=True)
    service_section5_content = models.TextField(max_length=500, null=True, blank=True)
    service_section5_image = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.service_type)

class Service_why_amorserv(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)
    point1 = models.CharField(max_length=150, null=True, blank=True)
    point2 = models.CharField(max_length=150, null=True, blank=True)
    point3 = models.CharField(max_length=150, null=True, blank=True)
    point4 = models.CharField(max_length=150, null=True, blank=True)
    point5 = models.CharField(max_length=150, null=True, blank=True)
    point6 = models.CharField(max_length=150, null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Service (why amorserv)"

    def __str__(self) -> str:
        return str(self.service_type)
    
class Blog_Post_Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog Post Categories"

    def __str__(self) -> str:
        return str(self.title)

class Blog_Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    category = models.ForeignKey(Blog_Post_Category, on_delete=models.SET_NULL, null=True, blank=True)
    para1 =models.TextField(max_length=500, null=True, blank=True)
    para2 =models.TextField(max_length=500, null=True, blank=True)
    para3 =models.TextField(max_length=500, null=True, blank=True)
    para4 = models.TextField(max_length=500, null=True, blank=True)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    number_likes = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog Posts"

    def __str__(self) -> str:
        return str(self.title)
    
class Blog_Post_Comment(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    blogPost = models.ForeignKey(Blog_Post, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Blog Post Comments"

    def __str__(self) -> str:
        return str(self.title)
    
class Contact_Enquiries(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Enquiries"

    def __str__(self) -> str:
        return str(self.full_name)
    
class Contact_Info(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Information"

    def __str__(self) -> str:
        return str(self.full_name)
    
class Faq(models.Model):
    question = models.CharField(max_length=150, null=True, blank=True)
    answer = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Frequently Asked Question"

    def __str__(self) -> str:
        return str(self.full_name)
    
class Terms_Condition(models.Model):
    pass
    




