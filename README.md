# HOW TO USE THIS SKELETON #
1. Copy & Paste: django-admin.py startproject --template https://github.com/9gix/djskel/zipball/master --extension py,md,gitignore projectname
2. Change the projectname to something else
3. Delete These "HOW TO USE THIS SKELETON" from README.md and update the file accordingly

# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.7
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

### Configure project ###
```bash
cp {{ project_name }}/__local_settings.py {{ project_name }}/local_settings.py
vi {{ project_name }}/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

