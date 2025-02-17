# Setting up your Django Development Environment : 

## Open the Anaconda Prompt  or cmd as Administrator:
```bash
conda create -n dj Django
conda activate dj
python --version
pip --version
python -m django --version
```

## Create your first Django Project: 
```bash
conda activate dj
django-admin startproject Auth_app
cd Auth_app
python manage.py runserver
```
` - Open your browser and go to http://127.0.0.1:8000/
` - You can run the development server on your desired port also.
