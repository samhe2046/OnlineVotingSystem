---

# Property Online Voting System

This project is an online voting system designed for property management purposes, such as conducting periodic surveys and event voting. The system is built using Python and Django and is deployed on a CentOS Linux server with MySQL as the database.

## Features
- **User registration and login**
- **Secure voting process**
- **Real-time vote counting**
- **Admin panel for managing votes and users**

## Prerequisites
- **Python 3.x**
- **Django 3.x or later**
- **MySQL**
- **CentOS Linux**

## Setup Instructions

### 1. Install Python 3 on CentOS
First, update your package list:
```bash
sudo yum update
```

Install the required development tools:
```bash
sudo yum groupinstall 'development tools'
sudo yum install openssl-devel bzip2-devel libffi-devel
```

Download and install Python 3:
```bash
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
sudo tar xzf Python-3.9.1.tgz
cd Python-3.9.1
sudo ./configure --enable-optimizations
sudo make altinstall
```

Verify the installation:
```bash
python3.9 -V
```

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/property-online-voting-system.git
cd property-online-voting-system
```

### 3. Set Up the Virtual Environment
```bash
python3.9 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure MySQL Database
Create a MySQL database and user for the project:
```sql
CREATE DATABASE voting_system;
CREATE USER 'voting_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON voting_system.* TO 'voting_user'@'localhost';
FLUSH PRIVILEGES;
```

Update the `settings.py` file with your database configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voting_system',
        'USER': 'voting_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

### 9. Access the Application
Open your browser and navigate to `http://your_server_ip:8000` to access the application.

## Deployment Instructions

### 1. Configure Nginx
Install Nginx:
```bash
sudo yum install nginx
```

Create an Nginx configuration file for your project:
```nginx
server {
    listen 80;
    server_name your_server_ip;

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project.sock;
    }

    location /static/ {
        alias /path/to/your/project/static/;
    }
}
```

### 2. Start and Enable Services
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

Your Django application should now be accessible via your server's IP address.

---
