import os

# Define the paths
current_folder = os.getcwd()
studos_app_folder = os.path.join(current_folder, "studos")
templates_folder = os.path.join(studos_app_folder, "templates")
base_file = os.path.join(templates_folder, "base.html")

# 1. The HTML content for the Navigation Bar (base.html)
html_content = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stu-dos | EdTech</title>
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;500;700;800&display=swap" rel="stylesheet">
    <style>
        /* Global Styles */
        body { margin: 0; font-family: 'Lora', serif; background-color: #f8f9fa; }
        
        /* Navigation Bar */
        .navbar {
            background-color: #2c3e50; /* Dark Blue-Grey */
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .nav-brand { 
            font-family: 'Poppins', sans-serif;
            font-size: 1.5rem; 
            font-weight: bold; 
            display: flex; 
            align-items: center; 
            text-decoration: none;
            color: white;
        }
        
        .nav-logo { height: 40px; margin-right: 10px; }

        .nav-links a {
            font-family: 'Poppins', sans-serif;
            color: #ecf0f1;
            text-decoration: none;
            margin-left: 20px;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover { color: #3498db; }
        
        .btn-nav {
            background-color: #3498db;
            padding: 8px 15px;
            border-radius: 4px;
        }
        .btn-nav:hover { background-color: #2980b9 !important; }

        /* Container for page content */
        .container { max-width: 1000px; margin: 0 auto; padding: 20px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="{% url 'landing' %}" class="nav-brand">
            Stu-dos
        </a>
        <div class="nav-links">
            <a href="{% url 'landing' %}">Home</a>
            <a href="{% url 'app' %}" class="btn-nav">Go to App</a>
        </div>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>
"""

# 2. Write the file
with open(base_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SUCCESS! base.html created at: {base_file}")