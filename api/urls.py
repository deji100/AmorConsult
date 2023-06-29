from django.urls import path
from .views import *

urlpatterns = [
    path('endpoints', allEndPoints, name='endpoints'),
    path('header', Header.as_view(), name='header'),
    path('home-client-section', HomeClient.as_view(), name='home client'),
    path('home-overwhelmed', HomeOverwhelmed.as_view(), name='home overwhelmed'),
    path('home-proposal', HomeProposal.as_view(), name='home-proposal'),
    path('home-service', HomeService.as_view(), name='home service'),
    path('home-step-process', HomeStepProcess.as_view(), name='home step process'),
    path('happy-customers', HomeHappyCustomer.as_view(), name='happy customers'),
    path('about-us', AboutUs.as_view(), name='about us'),
    path('about-team', AboutTeam.as_view(), name='about team'),
    path('about-partner', AboutPartner.as_view(), name='about partner'),
    path('portfolios', PortfolioView.as_view(), name='portfolios'),
    path('services', ServiceView.as_view(), name='services'),
    path('service-why-amorserv', ServiceWhyAmorservView.as_view(), name='service why amorserv'),
    path('blog-post-categories', BlogPostCategoryView.as_view(), name='blog post categories'),
    path('blog-post', BlogPostView.as_view(), name='blog post'),
    path('blog-post-comment', BlogPostCommentView.as_view(), name="blog post comment"),
    path('contact-enquiries', ContactEnquiriesView.as_view(), name='contact enquiries'),
    path('contact-info', ContactInfoView.as_view(), name='contact info'),
    path('faq', FaqView.as_view(), name='faq')
]
