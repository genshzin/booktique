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

### 2. Alur request dan response dalam aplikasi Django
![IMG_0155](https://github.com/user-attachments/assets/154dde39-6057-47cb-878f-d241bf75d0be)
Penjelasan:
1. Client mengirim request.
2. Django memproses request dan mencari pola URL yang cocok di urls.py.
3. urls.py mengarahkan request ke fungsi view yang sesuai di views.py.
4. views.py memproses request dan berinteraksi dengan models.py jika perlu mengakses data.
5. views.py memilih template HTML yang sesuai dan merender-nya dengan data.
6. Template HTML dirender menjadi respons.
7. Respons dikirimkan ke client.

### 3.  Fungsi git dalam pengembangan perangkat lunak
Sebagai Version Control, git dapat melacak perubahan dalam kode dari waktu ke waktu, di mana pengembang dapat melihat riwayat perubahan dan kembali ke versi sebelumnya jika diperlukan. Fitur clone repositori dapat menjadi back up dari proyek. Dengan git, pengembang dapat menggunggah kode ke situs layanan repositori git, contohnya adalah github. Git sangat berguna dalam kolaborasi. Fitur branch dapat memfasilitasi kerja sama antar anggota tim. Branch memungkinkan para pengembang mengerjakan proyek secara bersamaan pada branch yang terpisah dari branch utama. Selain itu, branch juga berguna untuk mengembangkan fitur atau bereksperimen tanpa takut merusak kode pada branch utama. Selain itu, terdapat merge yang memudahkan penggabungan perubahan, fitur, dll untuk dikembalikan ke branch utama. Dengan demikian, git dapat mengurangi konflik kode dan memudahkan resolusi ketika konflik terjadi.
   
### 4. Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django menggunakan python, di mana bahasa yang sudah sangat familiar dan beginner friendly. Django merupakan open source framework yang berarti kita dapat mengakses sumbernya secara bebas dan dapat berkontribusi tanpa ada biaya lisensi. Django memiliki banyak fitur built-in di mana dapat memudahkan kita dalam membangun aplikasi web dengan cepat tanpa harus membuat dari "scratch", salah satunya ORM. Django juga menyediakan fitur-fitur keamanan yang melindungin pengembang dari serangan. Selain fitur-fitur bawaannya yang banyak, Django juga sangat cepat dan memiliki kemampuan untuk menangani lalu lintas tinggi dengan baik. Django sudah memiliki komunitas yang besar, sehingga memudahkan kita dalam bekerja sama, menangani problem, dlll. Django memiliki arsitektur MTV yang memudahkan kita sebagai pengembang untuk mengerjakan proyek dengan rapih dan terstruktur. Yang terakhir, django sudah banyak dipakai di industri yang membuktikan bahwa django merupakan framework yang terpercaya.

### 5. Alasan model pada Django disebut sebagai ORM
Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena fungsinya yang memetakan objek Python ke tabel database. Dengan menggunakan model Django, struktur data dapat didefinisikan melalui kelas Python, di mana setiap kelas model merepresentasikan sebuah tabel database. ORM ini menyediakan lapisan abstraksi antara kode Python dan database, memungkinkan interaksi dengan database menggunakan sintaks Python tanpa perlu menulis SQL secara langsung. Keuntungan lainnya adalah kode yang ditulis menjadi lebih fleksibel dan tidak terikat pada sistem database tertentu, sehingga dapat bekerja dengan berbagai database seperti PostgreSQL, MySQL, SQLite, dan sebagainya. Selain itu, Django ORM juga mendukung manajemen skema otomatis, yang berarti dapat secara otomatis membuat, mengubah, dan menghapus tabel database berdasarkan definisi model. Dengan Query API, ORM memudahkan pelaksanaan operasi database kompleks melalui metode Python, tanpa memerlukan raw SQL. 
    

## Tugas 2
### Langkah-langkah implementasi form 
1. Sebelum membuat form, pastikan model ```Product``` menggunakan UUID sebagai primary key untuk menggantikan primary key berupa integer yang secara default auto-increment. Lalu, run ```python manage.py makemigrations``` dan ```python manage.py migrate```.
   
    ```python
   import uuid
   from django.db import models
   
   class Product(models.Model):
       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
       ...
    ```
2. Membuat Django form untuk ```Product``` model dengan membuat ```forms.py``` di dalam direktori ```main```.
   
   ```python
   from django import forms
   from .models import Product
   
   class ProductForm(forms.ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'author', 'description', 'stock_quantity', 'price']
    ```
3. Membuat method ```create_product``` untuk handle pembuatan produk baru ke dalam database.
   
   ```python
   def create_product(request):
       form = ProductForm(request.POST or None)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           return redirect('main:show_main')
   
       context = {'form': form}
       return render(request, "create_product.html", context)
    ```
4.  Untuk menggunakan views di atas, update ```urls.py``` di ```main``` untuk memasukan ```path``` untuk view di atas.
      ```python
         urlpatterns = [
             ...
             path('create_product/', create_product, name='create_product'),
             ...
         ]
      ```
6. Selanjutnya, buat template yang dibutuhkan, yaitu ```create_product.html``` dalam ```templates``` di direktori ```main```.
      ```html
      {% extends 'base.html' %}
      
      {% block meta %}
      <title>Add New Product - Booktique</title>
      {% endblock meta %}
      
      {% block content %}
      <h1>Add New Product</h1>
      
      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Product"/>
                  </td>
              </tr>
          </table>
      </form>
      
      <br />
      
      <a href="{% url 'main:show_main' %}">
          <button>Back to Product List</button>
      </a>
      
      {% endblock content %}
   ```
   
7. Sebelumnya, buat dahulu direktori ```templates``` di direktori utama dan tambahkan ```base.html```.
   
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
     </head>
   
     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```
8. Menambahkan lokasi direktori tersebut ke dalam ```settings.py``` di direktori ```booktique```.
   
   ```python
      ...
      'DIRS': [BASE_DIR / 'templates'],
      ...
   ```
   
9. Mengedit template ```main.html``` (ekstensi dari ```base.html```) untuk menampilkan daftar produk pada aplikasi Booktique dan menampilkan informasi produk dalam tabel, serta menyediakan tombol untuk menambahkan produk baru.
   ```html
   {% extends 'base.html' %}
   
   {% block meta %}
   <title>Booktique - Product List</title>
   {% endblock meta %}
   
   {% block content %}
   <h1>Booktique</h1>
   
   <h5>Name:</h5>
   <p>{{ name }}</p>
   
   <h5>Class:</h5>
   <p>{{ class }}</p>
   
   {% if not products %}
   <p>No products available in Booktique.</p>
   {% else %}
   <table>
     <tr>
       <th>Name</th>
       <th>Author</th>
       <th>Description</th>
       <th>Stock Quantity</th>
       <th>Price</th>
     </tr>
   
     {% for product in products %}
     <tr>
       <td>{{product.name}}</td>
       <td>{{product.author}}</td>
       <td>{{product.description}}</td>
       <td>{{product.stock_quantity}}</td>
       <td>{{product.price}}</td>
     </tr>
     {% endfor %}
   </table>
   {% endif %}
   
   <br />
   
   <a href="{% url 'main:create_product' %}">
     <button>Add New Product</button>
   </a>
   
   {% endblock content %}
   ```
10. Menambahkan 4 fungsi ```views``` untuk menampilkan data produk dalam format XML atau JSON, baik untuk semua produk maupun produk berdasarkan ID tertentu.
    
    ```python
      def show_xml(request):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      
      def show_json(request):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      
      def show_xml_by_id(request, id):
          data = Product.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      
      def show_json_by_id(request, id):
          data = Product.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
11. Menambahkan route di ```urls.py``` di ```main``` untuk mengakses fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id agar data dapat diambil dalam format XML atau JSON sesuai kebutuhan.

    ```python
      urlpatterns = [
          ...
          path('xml/', show_xml, name='show_xml'),
          path('json/', show_json, name='show_json'),
          path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
      ]
    ```
12.  Menguji aplikasi Django secara langsung di browser dengan alamat default  ```http://127.0.0.1:8000/```dengan run ```python manage.py runserver```.
### Jawaban pertanyaan
#### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery itu penting banget dalam implementasi platform karena pada dasarnya, platform apapun pasti melibatkan pertukaran data antara client dan server. Data delivery memastikan bahwa data yang dikirim dan diterima tepat waktu, akurat, dan bisa diakses dengan lancar. Bayangin aja kalau nggak ada mekanisme pengiriman data yang bagus, pasti platform-nya jadi lambat, error terus, atau malah nggak jalan sama sekali. Jadi, data delivery itu kunci untuk memastikan user experience tetap mulus.
#### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurutku, kalau dibandingin XML sama JSON, JSON lebih populer karena lebih simpel dan efisien. JSON itu lebih ringkas, gampang dibaca manusia dan lebih mudah di-parse oleh komputer. Sedangkan, XML lebih verbose (lebih banyak tag) dan cenderung bikin file lebih besar. Jadi, buat aplikasi modern yang butuh proses cepat dan ringan, JSON lebih cocok. Apalagi sekarang banyak framework yang udah native support JSON, makanya dia jadi lebih populer.
#### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` di Django itu buat ngecek apakah data yang diisi di form udah sesuai aturan (validasi) yang kita tentukan. Jadi, sebelum kita proses data form lebih lanjut (kayak disimpan ke database), kita cek dulu pake `is_valid()` biar pastiin nggak ada data yang salah format atau nggak sesuai. Kalau nggak ada validasi ini, bisa-bisa data yang disimpan berantakan, yang tentu bisa bikin error di aplikasi kita.
#### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` penting banget di Django buat ngelindungin aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF itu serangan di mana penyerang bisa ngerjain request jahat atas nama user tanpa sepengetahuan mereka, misalnya transfer uang atau hapus data penting. Nah, `csrf_token` ini mencegah hal itu dengan nge-verify setiap form submission berasal dari user yang sah (bukan penyerang). Kalau kita nggak pake `csrf_token`, penyerang bisa manfaatin celah ini buat ngejalanin aksi jahat dengan menyamar sebagai user kita. Jadi, token ini semacam pelindung biar aplikasi kita aman dari manipulasi.






    
     
