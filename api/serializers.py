from rest_framework.serializers import ModelSerializer
from .models import *

class HeaderSerializer(ModelSerializer):

    class Meta:
        model = Header_section
        fields = "__all__"

class Home_ClientSerializer(ModelSerializer):

    class Meta:
        model = Home_client_section
        fields = "__all__"

class Home_OverWhelmedSerializer(ModelSerializer):

    class Meta:
        model = Home_overwhelmed_section
        fields = "__all__"

class Home_ProposalSerializer(ModelSerializer):

    class Meta:
        model = Home_proposal_section
        fields = "__all__"

class Home_ServiceSerializer(ModelSerializer):

    class Meta:
        model = Home_service_section
        fields = "__all__"

class Home_Step_ProcessSerializer(ModelSerializer):

    class Meta:
        model = Home_step_process_section
        fields = "__all__"

class Home_Happy_CustomerSerializer(ModelSerializer):

    class Meta:
        model = Home_happy_customer
        fields = "__all__"

class About_UsSerializer(ModelSerializer):

    class Meta:
        model = About_Us
        fields = "__all__"

class About_TeamSerializer(ModelSerializer):

    class Meta:
        model = About_team
        fields = "__all__"

class About_PartnerSerializer(ModelSerializer):

    class Meta:
        model = About_partner
        fields = "__all__"

class PortfolioSerializer(ModelSerializer):

    class Meta:
        model = Portfolio
        fields = "__all__"

class ServiceSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

class Service_Why_AmorservSerializer(ModelSerializer):

    class Meta:
        model = Service_why_amorserv
        fields = "__all__"

class Blog_Post_CategorySerializer(ModelSerializer):

    class Meta:
        model = Blog_Post_Category
        fields = "__all__"

class Blog_PostSerializer(ModelSerializer):

    class Meta:
        model = Blog_Post
        fields = "__all__"

class Blog_Post_CommentSerializer(ModelSerializer):

    class Meta:
        model = Blog_Post_Comment
        fields = "__all__"

class Contact_EnquiriesSerializer(ModelSerializer):

    class Meta:
        model = Contact_Enquiries
        fields = "__all__"

class Contact_InfoSerializer(ModelSerializer):

    class Meta:
        model = Contact_Info
        fields = "__all__"

class FaqSerializer(ModelSerializer):

    class Meta:
        model = Faq
        fields = "__all__"
