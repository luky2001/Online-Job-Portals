from django.db import models
from django.contrib.auth.models import User

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)
    com_location = models.CharField(max_length=255)
    com_industry = models.CharField(max_length=100, choices=[
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ])
    com_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.company_name
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    job_position = models.CharField(max_length=255)
    job_description = models.TextField()
    job_category = models.CharField(max_length=100, choices=[
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ])
    job_location = models.CharField(max_length=255)
    job_salary = models.IntegerField(blank=True, null=True)
    job_experience = models.CharField(max_length=50, blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=[
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ])
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    ], default='Active')
    def __str__(self):
        return self.title
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.user.username
class JobApplication(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)
    def __str__(self):
        return f"{self.candidate.user.username} -> {self.job.job_position}"
