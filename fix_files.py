import os

# Define the paths
current_folder = os.getcwd()
studos_app_folder = os.path.join(current_folder, "studos")
templates_folder = os.path.join(studos_app_folder, "templates")
landing_file = os.path.join(templates_folder, "landing.html")

# 1. Create the 'templates' folder if it doesn't exist
if not os.path.exists(templates_folder):
    os.makedirs(templates_folder)
    print(f"Created folder: {templates_folder}")

# 2. The HTML content
html_content = """{% extends 'base.html' %}
{% load static %}

{% block content %}
<style>
    :root { --primary: #2c3e50; --accent: #e67e22; --light: #fdfbf7; }
    body { font-family: 'Lora', serif; background-color: var(--light); }
    h1, h2, h3, .btn { font-family: 'Poppins', sans-serif; }
    
    .hero { background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); color: white; padding: 100px 20px; text-align: center; }
    .hero h1 { font-size: 3.5rem; margin-bottom: 15px; }
    .btn-hero { background-color: var(--accent); color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; }
    
    .mv-container { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; max-width: 1000px; margin: 60px auto; padding: 20px; }
    .mv-card { background: white; padding: 40px; border-radius: 15px; border-top: 5px solid var(--primary); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    
    .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
    .service-card { background: white; padding: 25px; border-radius: 10px; border-left: 4px solid var(--accent); }
    .service-card a { text-decoration: none; color: var(--primary); font-size: 1.2rem; font-weight: bold; }
</style>

<div class="hero">
    <h1>From Struggle To Support</h1>
    <p style="font-size: 1.2rem; margin-bottom: 40px;">"Education teaches subjects. Opportunity demands skills. Stu-dos bridges the gap."</p>
    <a href="{% url 'app' %}" class="btn-hero">Start Your Journey</a>
</div>

<div class="mv-container">
    <div class="mv-card">
        <h3>🚀 Our Mission</h3>
        <p>To empower students—especially those from under-resourced backgrounds—by providing accessible academic, digital, and career support.</p>
    </div>
    <div class="mv-card" style="border-top-color: var(--accent);">
        <h3>👁️ Our Vision</h3>
        <p>To become a trusted student-support ecosystem that bridges education and employment through skills, services, and technology.</p>
    </div>
</div>

<div style="background: #f0f2f5; padding-bottom: 60px;">
    <div style="text-align: center; padding-top: 60px;">
        <h2>Services We Provide</h2>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <h4><a href="{% url 'service_academic' %}">📄 Academic Support</a></h4>
            <p>Xerox, printing, spiral binding, and professional typing.</p>
        </div>
        <div class="service-card">
            <h4><a href="{% url 'service_career' %}">💼 Career Readiness</a></h4>
            <p>ATS-friendly resumes, LinkedIn optimization, and cover letters.</p>
        </div>
        <div class="service-card">
            <h4><a href="{% url 'service_skills' %}">🗣️ Skill Development</a></h4>
            <p>Interview preparation and confidence building.</p>
        </div>
    </div>
</div>
{% endblock %}
"""

# 3. Force write the file
with open(landing_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SUCCESS! Landing page created at: {landing_file}")