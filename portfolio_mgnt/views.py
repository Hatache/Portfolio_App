from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.http import HttpResponse

# Create your views here.
from .models import Service,ContactMessage,MyProject, Skill, SkillCategory, AboutMe, WorkExperience, Education, HeroSection, ThemeSettings, Blog


def index(request):
    myprojects = MyProject.objects.all()
    about_me = AboutMe.objects.first()  # Get the first (and should be only) AboutMe instance
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    work_experiences = WorkExperience.objects.all()
    education = Education.objects.all()
    hero_section = HeroSection.objects.first()
    theme_settings = ThemeSettings.objects.first()
    
    context = {
        'myprojects': myprojects,
        'skill_categories': skill_categories,
        'about_me': about_me,
        'work_experiences': work_experiences,
        'education': education,
        'hero': hero_section,
        'theme': theme_settings,
    }
    return render(request, 'index.html', context)


def service(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/#contact')
    
    return redirect('/#contact') 

def blog_list(request):
    blog_posts = Blog.objects.filter(is_published=True)
    theme_settings = ThemeSettings.objects.first()
    
    context = {
        'blog_posts': blog_posts,
        'theme': theme_settings,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, is_published=True)
    theme_settings = ThemeSettings.objects.first()
    
    # Get next and previous posts
    next_post = Blog.objects.filter(
        created_at__gt=post.created_at,
        is_published=True
    ).order_by('created_at').first()
    
    previous_post = Blog.objects.filter(
        created_at__lt=post.created_at,
        is_published=True
    ).order_by('-created_at').first()
    
    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
        'theme': theme_settings,
    }
    return render(request, 'blog_detail.html', context) 
