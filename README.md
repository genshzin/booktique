# Booktique

Booktique adalah aplikasi web berbasis Django yang dirancang sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform. Proyek ini dibuat oleh Nasha Zahira (2306165553). 
## Tugas 2
### 1. Langkah-langkah membuat proyek Django
Proyek dibuat dengan langkah-langkah sebagai berikut:

1. Membuat repositori daring (Github) bernama ```booktique```.
2. Clone repositori tersebut ke komputer lokal.
3. Pada direktori lokal ```booktique```, buka command prompt lalu menjalankan perintah di bawah ini untuk membuat virtual environment

   ```bash
    python -m venv env
    ```
5. Melakukan aktivasi virtual environment.
   
   ```bash
    env\Scripts\activate
    ```
6. Membuat file ```requirement.txt```, lalu isi dengan:
   
   ```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
7. Installasi dependensi.
   
   ```bash
    pip install -r requirements.txt
    ```
8. Membuat proyek Django bernama ```booktique``` dengan menjalani perintah berikut.
   
   ```bash
   django-admin startproject booktique .
   ```
9. Untuk server deployment, tambahkan host server ke ALLOWED_HOSTS.
    
   ```bash
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
10. Membuat aplikasi baru bernama ```main``` di dalam proyek Django.
     
      ```bash
      python manage.py startapp main
      ```
11. Daftarkan aplikasi  ```main``` di settings.py ke dalam  ```INSTALLED_APPS```.
    
      ```bash
      INSTALLED_APPS = [
       ...
       'main',
      ]
      ```
12. Membuat model pada aplikasi main dengan mengubah ```models.py``` menjadi berikut.

      ```python
      from django.db import models
      
      class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.IntegerField()
          description = models.TextField()
          stock_quantity = models.IntegerField()
          author = models.CharField(max_length=255)

      ```
13. Setelah model dibuat, buat file migrasi.
    
     ```bash
      python manage.py makemigrations

      ```
14. Melakukan migrasi untuk menerapkan perubahan ke database.
    
     ```bash
     python manage.py migrate

      ```
15. Membuat direktori baru ```templates``` di ```main``` dan membuat file html baru ```main.html``` di dalam direktori tersebut.
    
    ```html
     <h1>{{ app_name }}</h1>

      <h5>Name: </h5>
      <p>{{ name }}<p>
      <h5>Class: </h5>
      <p>{{ class }}<p>

      ```
16. Di folder aplikasi ```main```, saya membuat fungsi view di dalam ```views.py``` untuk ```rendering``` template dengan konteks, di mana data dari view dikirim ke template HTML untuk ditampilkan.
    
    ```python
      from django.shortcuts import render
    
      def show_main(request):
          context = {
              'app_name' : 'Booktique',
              'name': 'Nasha Zahira',
              'class': 'PBP B'
          }

          return render(request, "main.html", context)

      ```
17. Melakukan routing pada proyek dalam file ```urls.py``` di direktori proyek ```booktique```.

    ```python
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('main.urls'))
      ]
      ```
18.  Melakukan routing pada aplikasi dalam file ```urls.py``` di direktori aplikasi ```main```.

       ```python
          from django.urls import path
          from main.views import show_main
      
          app_name = 'main'
      
          urlpatterns = [
              path('', show_main, name='show_main'),
          ]
       ```
19. Menguji aplikasi Django secara langsung di browser dengan alamat default  ```http://127.0.0.1:8000/```.
    
21. Menambahkan berkas ```.gitignore``` di dalam direktori utama yang berisi:
    ```bash
      # Django
      *.log
      *.pot
      *.pyc
      __pycache__
      db.sqlite3
      media
      
      # Backup files
      *.bak
      
      # If you are using PyCharm
      # User-specific stuff
      .idea/**/workspace.xml
      .idea/**/tasks.xml
      .idea/**/usage.statistics.xml
      .idea/**/dictionaries
      .idea/**/shelf
      
      # AWS User-specific
      .idea/**/aws.xml
      
      # Generated files
      .idea/**/contentModel.xml
      .DS_Store
      
      # Sensitive or high-churn files
      .idea/**/dataSources/
      .idea/**/dataSources.ids
      .idea/**/dataSources.local.xml
      .idea/**/sqlDataSources.xml
      .idea/**/dynamic.xml
      .idea/**/uiDesigner.xml
      .idea/**/dbnavigator.xml
      
      # Gradle
      .idea/**/gradle.xml
      .idea/**/libraries
      
      # File-based project format
      *.iws
      
      # IntelliJ
      out/
      
      # JIRA plugin
      atlassian-ide-plugin.xml
      
      # Python
      *.py[cod]
      *$py.class
      
      # Distribution / packaging
      .Python build/
      develop-eggs/
      dist/
      downloads/
      eggs/
      .eggs/
      lib/
      lib64/
      parts/
      sdist/
      var/
      wheels/
      *.egg-info/
      .installed.cfg
      *.egg
      *.manifest
      *.spec
      
      # Installer logs
      pip-log.txt
      pip-delete-this-directory.txt
      
      # Unit test / coverage reports
      htmlcov/
      .tox/
      .coverage
      .coverage.*
      .cache
      .pytest_cache/
      nosetests.xml
      coverage.xml
      *.cover
      .hypothesis/
      
      # Jupyter Notebook
      .ipynb_checkpoints
      
      # pyenv
      .python-version
      
      # celery
      celerybeat-schedule.*
      
      # SageMath parsed files
      *.sage.py
      
      # Environments
      .env
      .venv
      env/
      venv/
      ENV/
      env.bak/
      venv.bak/
      
      # mkdocs documentation
      /site
      
      # mypy
      .mypy_cache/
      
      # Sublime Text
      *.tmlanguage.cache
      *.tmPreferences.cache
      *.stTheme.cache
      *.sublime-workspace
      *.sublime-project
      
      # sftp configuration file
      sftp-config.json
      
      # Package control specific files Package
      Control.last-run
      Control.ca-list
      Control.ca-bundle
      Control.system-ca-bundle
      GitHub.sublime-settings
      
      # Visual Studio Code
      .vscode/*
      !.vscode/settings.json
      !.vscode/tasks.json
      !.vscode/launch.json
      !.vscode/extensions.json
      .history

      ```
22. Melakukan git ```add```, ```commit```, dan ```push```.
23. Melakukan deployment melalui PWS (Pacil Web Service).

Langkah-langkah deployement:
1. Login PWS pada https://pbp.cs.ui.ac.id/
2. Membuat project baru bernama ```booktique```.
3. Menambahkan URL deployment ```http://nasha-zahira-booktique.pbp.cs.ui.ac.id/``` ke dalam ```ALLOWED_HOSTS```.
4. Melakukan git ```add```, ```commit```, dan ```push```.
5. Menjalankan ```Project Command``` yang ada pada PWS.
6. Mengubah branch menjadi ```main``` lagi.

### Alur request dan response dalam aplikasi Django

   
    
    
    
   
   
