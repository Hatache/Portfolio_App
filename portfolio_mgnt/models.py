from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class MyProject(models.Model):
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    demo_link = models.URLField(max_length=200)
    git_link = models.URLField(max_length=200)
    technologies = models.CharField(max_length=500, null=True, blank=True, help_text="Enter technologies separated by commas (e.g., React, Node.js, MongoDB)")
    
    def get_technologies(self):
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []

    def __str__(self):
        return self.project_title


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome class name (e.g., 'fas fa-code')")
    order = models.IntegerField(default=0, help_text="Order in which the category should appear")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        SkillCategory, 
        on_delete=models.CASCADE, 
        related_name='skills',
        null=True,  # Allow null temporarily for migration
        blank=True
    )
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency level (0-100)"
    )
    order = models.IntegerField(default=0, help_text="Order in which the skill should appear within its category")

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.category.name if self.category else 'Uncategorized'})"

class AboutMe(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    interests = models.TextField(help_text="Enter interests separated by commas")

    def get_interests(self):
        if self.interests:
            return [interest.strip() for interest in self.interests.split(',')]
        return []

    class Meta:
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.full_name

class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank for current position")
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Order in which this experience should appear")

    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"

    def __str__(self):
        return f"{self.title} at {self.company}"
    
    def get_duration(self):
        if self.end_date:
            return f"{self.start_date.year} - {self.end_date.year}"
        return f"{self.start_date.year} - Present"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if still studying")
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Order in which this education should appear")

    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
    def get_duration(self):
        if self.end_date:
            return f"{self.start_date.year} - {self.end_date.year}"
        return f"{self.start_date.year} - Present"

class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='hero/', help_text="Profile image for hero section")
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.name

class ThemeSettings(models.Model):
    # Primary Colors
    primary_color = models.CharField(max_length=7, default="#0d6efd", help_text="Primary theme color (e.g., #0d6efd)")
    secondary_color = models.CharField(max_length=7, default="#6c757d", help_text="Secondary theme color")
    accent_color = models.CharField(max_length=7, default="#240303", help_text="Accent color for highlights")
    
    # Background Colors
    background_color = models.CharField(max_length=7, default="#ffffff", help_text="Main background color")
    section_bg_light = models.CharField(max_length=7, default="#f8f9fa", help_text="Light section background")
    section_bg_dark = models.CharField(max_length=7, default="#212529", help_text="Dark section background")
    
    # Text Colors
    text_color_light = models.CharField(max_length=7, default="#ffffff", help_text="Light text color")
    text_color_dark = models.CharField(max_length=7, default="#212529", help_text="Dark text color")
    
    # Font Settings
    heading_font = models.CharField(
        max_length=100, 
        default="'Poppins', sans-serif",
        help_text="Font family for headings (e.g., 'Poppins', sans-serif)"
    )
    body_font = models.CharField(
        max_length=100, 
        default="'Open Sans', sans-serif",
        help_text="Font family for body text"
    )
    
    # Font Sizes
    heading_size = models.CharField(max_length=10, default="2.5rem", help_text="Size for main headings (e.g., 2.5rem)")
    subheading_size = models.CharField(max_length=10, default="1.8rem", help_text="Size for sub-headings")
    body_size = models.CharField(max_length=10, default="1rem", help_text="Size for body text")
    
    class Meta:
        verbose_name = "Theme Settings"
        verbose_name_plural = "Theme Settings"

    def __str__(self):
        return "Theme Settings"
    
    def save(self, *args, **kwargs):
        if not self.pk and ThemeSettings.objects.exists():
            # if you're trying to create a new settings instance but one already exists
            return ThemeSettings.objects.first()
        return super(ThemeSettings, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title")
    summary = models.TextField(help_text="A brief summary of the blog post")
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', help_text="Cover image for the blog post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    read_time = models.IntegerField(default=5, help_text="Estimated reading time in minutes")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


