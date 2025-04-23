from django.contrib import admin
from .models import (
    Service, ContactMessage, MyProject, Skill, SkillCategory, 
    AboutMe, WorkExperience, Education, HeroSection, ThemeSettings, Blog
)

class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_description', 'image', 'demo_link', 'git_link')
    search_fields = ('project_title', 'project_description')
    
    fieldsets = (
        ('Project Information', {
            'fields': ('project_title', 'project_description', 'image')
        }),
        ('Project Details', {
            'fields': ('technologies', 'demo_link', 'git_link')
        }),
    )

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    ordering = ('order', 'name')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order', 'get_skills_count')
    list_editable = ('order',)
    search_fields = ('name',)
    inlines = [SkillInline]
    
    def get_skills_count(self, obj):
        return obj.skills.count()
    get_skills_count.short_description = 'Number of Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    list_editable = ('proficiency', 'order')
    search_fields = ('name',)
    ordering = ('category', 'order', 'name')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'location', 'availability')
    fieldsets = (
        ('Basic Information', {
            'fields': ('full_name', 'title', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'location', 'availability')
        }),
        ('Additional Information', {
            'fields': ('resume', 'interests')
        }),
    )

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'get_duration', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'company', 'description')
    ordering = ('-start_date', 'order')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'get_duration', 'order')
    list_editable = ('order',)
    search_fields = ('degree', 'institution', 'description')
    ordering = ('-start_date', 'order')
    fieldsets = (
        ('Basic Information', {
            'fields': ('degree', 'institution')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
    )

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'subtitle')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'subtitle')
        }),
        ('Content', {
            'fields': ('description', 'profile_image')
        }),
    )

    def has_add_permission(self, request):
        # Check if there's already a hero section
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Colors', {
            'fields': (
                ('primary_color', 'secondary_color', 'accent_color'),
                ('background_color',),
                ('section_bg_light', 'section_bg_dark'),
                ('text_color_light', 'text_color_dark'),
            ),
            'description': 'Customize the color scheme of your portfolio. Use hex color codes (e.g., #0d6efd).'
        }),
        ('Typography', {
            'fields': (
                ('heading_font', 'body_font'),
                ('heading_size', 'subheading_size', 'body_size'),
            ),
            'description': 'Customize the fonts and text sizes. For fonts, use web-safe fonts or Google Fonts names.'
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance of theme settings
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the theme settings
        return False

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'read_time')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'summary', 'image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'read_time')
        }),
    )

# Customizing the admin branding
admin.site.site_header = "Portfolio Management"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Portfolio Administration"

# Register models
admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Service)
admin.site.register(ContactMessage)
