
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import Header_section

# Create your views here.

@api_view(['GET'])
def allEndPoints(request):
    endpoints = ['header',
                 'home-client-section',
                 'home-overwhelmed',
                 'home-proposal',
                 'home-service',
                 'home-step-process',
                 'happy-customers',
                 'about-us',
                 'about-team',
                 'about-partner',
                 'portfolios',
                 'services',
                 'service-why-amorserv',
                 'blog-post-categories',
                 'blog-post',
                 'blog-post-comment',
                 'contact-enquiries',
                 'contact-info',
                 'faq']
    return Response(endpoints)

class Header(generics.ListAPIView):
    queryset = Header_section.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [AllowAny]

class HomeClient(generics.ListAPIView):
    queryset = Home_client_section.objects.all()
    serializer_class = Home_ClientSerializer
    permission_classes = [AllowAny]

class HomeClient(generics.ListAPIView):
    queryset = Home_client_section.objects.all()
    serializer_class = Home_ClientSerializer
    permission_classes = [AllowAny]

class HomeOverwhelmed(generics.ListAPIView):
    queryset = Home_overwhelmed_section.objects.all()
    serializer_class = Home_OverWhelmedSerializer
    permission_classes = [AllowAny]

class HomeProposal(generics.ListAPIView):
    queryset = Home_proposal_section.objects.all()
    serializer_class = Home_ProposalSerializer
    permission_classes = [AllowAny]

class HomeService(generics.ListAPIView):
    queryset = Home_service_section.objects.all()
    serializer_class = Home_ServiceSerializer
    permission_classes = [AllowAny]

class HomeStepProcess(generics.ListAPIView):
    queryset = Home_step_process_section.objects.all()
    serializer_class = Home_Step_ProcessSerializer
    permission_classes = [AllowAny]

class HomeHappyCustomer(generics.ListAPIView):
    queryset = Home_happy_customer.objects.all()
    serializer_class = Home_Happy_CustomerSerializer
    permission_classes = [AllowAny]

class AboutUs(generics.ListAPIView):
    queryset = About_Us.objects.all()
    serializer_class = About_UsSerializer
    permission_classes = [AllowAny]

class AboutTeam(generics.ListAPIView):
    queryset = About_team.objects.all()
    serializer_class = About_TeamSerializer
    permission_classes = [AllowAny]

class AboutPartner(generics.ListAPIView):
    queryset = About_partner.objects.all()
    serializer_class = About_PartnerSerializer
    permission_classes = [AllowAny]

class PortfolioView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [AllowAny]

class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

class ServiceWhyAmorservView(generics.ListAPIView):
    queryset = Service_why_amorserv.objects.all()
    serializer_class = Service_Why_AmorservSerializer
    permission_classes = [AllowAny]

class BlogPostCategoryView(generics.ListAPIView):
    queryset = Blog_Post_Category.objects.all()
    serializer_class = Blog_Post_CategorySerializer
    permission_classes = [AllowAny]

class BlogPostView(generics.ListAPIView):
    queryset = Blog_Post.objects.all()
    serializer_class = Blog_PostSerializer
    permission_classes = [AllowAny]

class BlogPostCommentView(generics.ListAPIView):
    queryset = Blog_Post_Comment.objects.all()
    serializer_class = Blog_Post_CommentSerializer
    permission_classes = [AllowAny]

class ContactEnquiriesView(generics.ListCreateAPIView):
    queryset = Contact_Enquiries.objects.all()
    serializer_class = Contact_EnquiriesSerializer
    permission_classes = [AllowAny]

class ContactInfoView(generics.ListCreateAPIView):
    queryset = Contact_Info.objects.all()
    serializer_class = Contact_InfoSerializer
    permission_classes = [AllowAny]

class FaqView(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = [AllowAny]