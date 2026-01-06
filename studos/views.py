from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, AssistanceRequest
from .forms import TaskForm

# --- 1. MAIN PAGES ---

def landing(request):
    """
    Renders the landing page and handles the 'Need Assistance' form.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')

        if name and phone:
            AssistanceRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service
            )
            return redirect('landing') # Reload to clear form

    return render(request, 'landing.html')


def about(request):
    """
    Renders the About Us page.
    """
    return render(request, 'about.html')


def contact(request):
    """
    Renders the Contact page and handles the contact form submission.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        # Note: We aren't saving 'message' yet because the model doesn't have it.
        # We only save the fields that exist in the database.

        if name and phone:
            AssistanceRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service
            )
            return redirect('contact')

    return render(request, 'contact.html')


# --- 2. SERVICE PAGES ---
# Each view renders its specific HTML template

def service_resume(request):
    return render(request, 'services_resume.html') 

def service_application(request):
    return render(request, 'services_application.html')

def service_career(request):
    return render(request, 'services_career.html')

def service_academic(request):
    return render(request, 'services_academic.html')

def service_skills(request):
    return render(request, 'services_skills.html')

def service_digital(request):
    return render(request, 'services_digital.html')


# --- 3. ORIGINAL APP (TODO LIST) ---

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app')
    else:
        form = TaskForm()

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('app')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('app')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        
        # --- GET THE MESSAGE ---
        message = request.POST.get('message') 

        if name and phone:
            AssistanceRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service,
                message=message  # <--- SAVE IT HERE
            )
            return redirect('contact')

    return render(request, 'contact.html')