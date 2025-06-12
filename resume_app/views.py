from django.shortcuts import render
from .models import Summary, Education, Certification, Project

def resume_view(request):
    summary = Summary.objects.first()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    projects = Project.objects.all()
    return render(request, 'resume.html', {
        'summary': summary,
        'education': education,
        'certifications': certifications,
        'projects': projects
    })
