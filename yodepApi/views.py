from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status 
from yodepApi.models import Events, Project, Testimonial, Career, Gallary, News, Events, Blog, Comment, Partner, Vacancy
from yodepApi.serializer import UserSerializer, RegisterSerializer, TestimonialSerializer, ProjectSerializer, CareerSerializer, GallarySerializer, NewsSerializer, EventsSerializer, BlogSerializer, CommentSerializer, PartnerSerializer, VacancySerializer 
from rest_framework.views import APIView

from rest_framework import generics, permissions
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login


def index(request):
    return render(request, 'yodepApi/index.html')

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# Login user
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




#testimonies. 
class TestimonialList(APIView):

    def get(self, request):
        testimonial = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonial, many = True)
        return Response(serializer.data) 

class TestimonialCreate(APIView):
    def post(self, request): 
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestimonialDetail(APIView):

    def get_testimonial_by_pk(self, pk):
            return Testimonial.objects.get(pk=pk)

    def get(self, request , pk):

        try:
            testimonial = self.get_testimonial_by_pk(pk)
            serializer = TestimonialSerializer(testimonial)
            return Response(serializer.data)

        except:
            return Response({
                'error':'Testimonial not found'
            }, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        testimonial = self.get_testimonial_by_pk(pk)
        serializer = TestimonialSerializer(testimonial, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        testimonial = self.get_testimonial_by_pk(pk)
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# project
class ProjectList(APIView):
    def get(self, request):

        project = Project.objects.all()
        serializer = ProjectSerializer(project, many = True)
        return Response(serializer.data) 

class ProjectCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    def get_project_by_pk(self, pk):
        return Project.objects.get(pk=pk)

    def get(self, request , pk):

        try:
            project = self.get_project_by_pk(pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)

        except:
            return Response({
                'error':'Project not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, pk):
        project = self.get_project_by_pk(pk)
        serializer = ProjectSerializer(project, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        project = self.get_project_by_pk(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Career

class CareerList(APIView):
    def get(self, request):

        career = Career.objects.all()
        serializer = CareerSerializer(career, many = True)
        return Response(serializer.data) 

class CareerCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = CareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CareerDetail(APIView):

    def get_career_by_pk(self, pk):
        return Career.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            career = self.get_career_by_pk(pk)
            serializer = CareerSerializer(career)
            return Response(serializer.data)
        except:
            return Response({
                'error':'career not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request , pk):
        career = self.get_career_by_pk(pk)
        career.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Gallary
class ImageList(APIView):
    def get(self, request):
        image = Gallary.objects.all()
        serializer = GallarySerializer(image, many = True)
        return Response(serializer.data) 

class ImageCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = GallarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(APIView):

    def get_image_by_pk(self, pk):
           return Gallary.objects.get(pk=pk)

    def get(self, request, pk):
        try:
            image = self.get_image_by_pk(pk)
            serializer = GallarySerializer(image)
            return Response(serializer.data)
        except:
            return Response({
                'error':'image not found'
            }, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        image = self.get_image_by_pk(pk)
        serializer = GallarySerializer(image, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        image = self.get_image_by_pk(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# news and insights
class NewsList(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many = True)
        return Response(serializer.data) 

class NewsCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDetail(APIView):
    def get_news_by_pk(self, pk):
           return News.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            news = self.get_news_by_pk(pk)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        except:
            return Response({
                'error':'News not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        news = self.get_news_by_pk(pk)
        serializer = NewsSerializer(news, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        news = self.get_news_by_pk(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# events

class EventsList(APIView):
    def get(self, request):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many = True)
        return Response(serializer.data) 

class EventCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    def get_event_by_pk(self, pk):
           return Events.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            event = self.get_event_by_pk(pk)
            serializer = EventsSerializer(event)
            return Response(serializer.data)
        except:
            return Response({ 
                'error':'Event not found'
            }, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        event = self.get_event_by_pk(pk)
        serializer = EventsSerializer(event, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        event = self.get_event_by_pk(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# blog

class BlogList(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many = True)
        return Response(serializer.data) 

class BlogCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    def get_blog_by_pk(self, pk):
           return Blog.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            blog = self.get_blog_by_pk(pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except:
            return Response({ 
                'error':'Blog not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        blog = self.get_blog_by_pk(pk)
        serializer = BlogSerializer(blog, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        blog = self.get_blog_by_pk(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# comment 

class CommentList(APIView):
    def get(self, request):
        comment =Comment.objects.all()
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data) 

class CommentCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_comment_by_pk(self, pk):
           return Comment.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            comment = self.get_comment_by_pk(pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except:
            return Response({ 
                'error':'comment not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request , pk):
        comment = self.get_comment_by_pk(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# partner

class PartnerList(APIView):
    def get(self, request):
        partner = Partner.objects.all()
        serializer = PartnerSerializer(partner, many = True)
        return Response(serializer.data) 

class PartnerCreate(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PartnerDetail(APIView):
    def get_partner_by_pk(self, pk):
           return Partner.objects.get(pk=pk)

    def get(self, request , pk):
        try:
            partner = self.get_partner_by_pk(pk)
            serializer = PartnerSerializer(partner)
            return Response(serializer.data)
        except:
            return Response({ 
                'error':'partner not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        partner = self.get_partner_by_pk(pk)
        serializer = PartnerSerializer(partner, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        partner = self.get_partner_by_pk(pk)
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# vacancy. 

class VacancyList(APIView):
    def get(self, request):

        vacancy = Vacancy.objects.all()
        serializer = VacancySerializer(vacancy, many = True)
        return Response(serializer.data) 

class VacancyCreate(APIView):

    # permission_classes = (IsAuthenticated, )
    def post(self, request): 
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyDetail(APIView):

    def get_vacancy_by_pk(self, pk):
            return Vacancy.objects.get(pk=pk)

    def get(self, request , pk):

        try:
            vacancy = self.get_vacancy_by_pk(pk)
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data)

        except:
            return Response({
                'error':'Vacancy not found'
            }, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        vacancy = self.get_vacancy_by_pk(pk)
        serializer = VacancySerializer(vacancy, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        vacancy = self.get_vacancy_by_pk(pk)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)