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
    

## Tugas 3
### Jawaban pertanyaan
#### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery itu memiliki peran penting dalam implementasi platform karena pada dasarnya, platform apapun pasti ada pertukaran data antara client dan server. Data delivery membuat data yang dikirim dan diterima jadi tepat waktu, akurat, dan bisa diakses dengan lancar. Bayangin saja kalau tidak ada mekanisme pengiriman data yang bagus, pasti platform-nya jadi lambat, error terus, atau malah tidak jalan sama sekali. Jadi, data delivery itu kunci untuk memastikan user experience tetap lancar.
#### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurutku, kalau dibandingin XML sama JSON, JSON lebih populer karena lebih simpel dan efisien. JSON itu lebih ringkas, gampang dibaca manusia dan lebih mudah di-parse oleh komputer. Sedangkan, XML lebih verbose (lebih banyak tag) dan cenderung bikin file lebih besar. Jadi, buat aplikasi modern yang butuh proses cepat dan ringan, JSON lebih cocok. Apalagi sekarang banyak framework yang udah native support JSON, makanya JSON jadi lebih populer.
#### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` di Django itu buat ngecek apakah data yang diisi di form udah sesuai aturan (validasi) yang kita tentukan. Jadi, sebelum kita proses data form lebih lanjut (seperti disimpan ke database), kita cek dulu pake `is_valid()` buat pastiin tidak ada data yang salah format atau tidak sesuai. Kalau tidak ada validasi ini, bisa-bisa data yang disimpan berantakan, yang tentu bisa bikin error di aplikasi kita.
#### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` penting banget di Django buat ngelindungin aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF itu serangan di mana penyerang bisa ngerjain request "jahat" atas nama user tanpa sepengetahuan mereka, misalnya transfer uang atau hapus data penting. Nah, `csrf_token` ini mencegah hal itu dengan nge-verify setiap form submission berasal dari user yang sah (bukan penyerang). Kalau kita nggak pake `csrf_token`, penyerang bisa manfaatin celah ini buat ngejalanin aksi jahat dengan menyamar sebagai user kita. Jadi, token ini semacam pelindung biar aplikasi kita aman dari manipulasi.

#### 5. Langkah-langkah implementasi form 
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

#### Screenshots postman
##### 1. XML
![Screenshot (354)](https://github.com/user-attachments/assets/67c97e45-5e16-4cc4-bb5e-388e65aa1e47)

##### 2. XML by ID
![Screenshot (355)](https://github.com/user-attachments/assets/93ae1524-09ee-4bf9-a7d3-34c671b9b03e)

##### 3. JSON
![Screenshot (356)](https://github.com/user-attachments/assets/caea1908-b584-4b09-a450-9a1049572e89)

##### 4. JSON by ID
![Screenshot (357)](https://github.com/user-attachments/assets/eb414af9-67cd-44b2-8886-4b88fcd4d86e)

## Tugas 4
### Apa perbedaan antara HttpResponseRedirect() dan redirect()

- **`HttpResponseRedirect()`**:
Ini adalah fungsi bawaan Django yang gunanya untuk melakukan redirect (pengalihan) dari satu URL ke URL lain. Jadi, ini bisa arahkan user dari halaman A ke halaman B. Tapi, untuk pakai ini, kita harus kasih URL secara manual. Contohnya:  
  ```python
  from django.http import HttpResponseRedirect
  return HttpResponseRedirect('/home/')
  ```

- **`redirect()`**
Nah, ini versi lebih simpel dan "upgrade" dari `HttpResponseRedirect()`. Dengan `redirect()`, kita bisa langsung kasih URL, nama view, atau bahkan objek, dan Django bakal otomatis tahu ke mana harus diarahkan. Jadi lebih fleksibel. Contohnya:  
  ```python
  from django.shortcuts import redirect
  return redirect('home')
  ```

### Jelaskan cara kerja penghubungan model Product dengan User!
Di Django, biasanya model `Product` bisa dihubungkan ke `User` (pengguna) menggunakan **ForeignKey**. Misalnya, kita mau tiap produk punya pemilik atau creator yang berasal dari `User`. Caranya, di model `Product`, kita tinggal tambahkan field `ForeignKey` yang merujuk ke model `User`. Contohnya:

```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Jadi, setiap produk bakal punya satu user. `on_delete=models.CASCADE` berarti kalau pengguna dihapus, produk yang dia buat juga bakal dihapus.


### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- Authentication: Ini kayak ngecek "Lu siapa sih?" Pas login, Django ngecek username sama password benar atau tidak.
- Authorization: Nah kalo ini lebih ke "Lu boleh ngapain aja?" Misal, cuma admin yang boleh hapus post.

Django punya system bawaan buat dua-duanya. Pas login, dia ngelakuin authentication dulu. Abis itu, dia bisa pake decorators kayak `@login_required` atau `@permission_required` buat authorization.
Pas pengguna login, yang dilakukan Django adalah **authentication** dulu. Jika autentikasi berhasil, baru si pengguna itu dapat **authorization** berdasarkan peran atau izin yang dia punya.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django pake session buat ini. Intinya, pas login berhasil, Django nyimpen info user di session (yang disimpen di database atau cache). Terus dia ngirim cookie ke browser yang isinya session ID. Setiap kali user kirim request baru, session ID itu dicek, dan Django tahu siapa user-nya tanpa harus login lagi.

#### Kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
 Selain buat session, cookies juga bisa dipakai buat banyak hal lain, misalnya:
  - Mengingat preferensi pengguna: Seperti bahasa yang dipilih atau tema warna.
  - Melacak aktivitas pengguna: Ini sering dipakai di website e-commerce buat nge-track barang apa yang pernah dilihat atau dimasukkan ke keranjang.

 **Apakah semua cookies aman digunakan?**
Gak semua cookies aman. Cookies bisa berisi data sensitif, jadi ada risiko kalau gak di-manage dengan benar. Ada juga yang namanya "third-party cookies" yang bisa dipake buat tracking lintas situs, makanya banyak browser mulai ngeblok ini. Hati-hati juga dengan cookies yang disimpan terlalu lama, karena bisa jadi sasaran bagi hacker buat eksploitasi.
Intinya, hati-hati aja sama data sensitif di cookies. Kalo mau aman, encrypt dulu atau mending simpen di server aja sekalian.

### Langkah-langkah implementasi
1. Membuat fungsi register, login, dan logout pada ```views.py``` di direktori ```main```.

    ```python
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

   def login_user(request):
      if request.method == 'POST':
         form = AuthenticationForm(data=request.POST)
   
         if form.is_valid():
               user = form.get_user()
               login(request, user)
               return redirect('main:show_main')
   
      else:
         form = AuthenticationForm(request)
      context = {'form': form}
      return render(request, 'login.html', context)
   
   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```
3. Melakukan routing url pada ```urls.py``` di direktori ```main``` untuk mengarahkan ke fungsi yang sudah dibuat.
   
   ```python
   urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
   ]
   ```
4. Menyesuaikan file html yang dibutuhkan seperti membuat ```register.html.``` dan ```login.html``` serta memodifikasi ```main.html``` untuk logout pada direktori ```main/templates```
  
   ```login.html```:
   ```html
   {% extends 'base.html' %}
   
   {% block meta %}
   <title>Login</title>
   {% endblock meta %}
   
   {% block content %}
   <div class="login">
     <h1>Login</h1>
   
     <form method="POST" action="">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input class="btn login_btn" type="submit" value="Login" /></td>
         </tr>
       </table>
     </form>
   
     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %} Don't have an account yet?
     <a href="{% url 'main:register' %}">Register Now</a>
   </div>
   
   {% endblock content %}
   ```
   ```register.html```:
   ```html
   {% extends 'base.html' %}
   
   {% block meta %}
   <title>Register</title>
   {% endblock meta %}
   
   {% block content %}
   
   <div class="login">
     <h1>Register</h1>
   
     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input type="submit" name="submit" value="Daftar" /></td>
         </tr>
       </table>
     </form>
   
     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %}
   </div>
   
   {% endblock content %}{% extends 'base.html' %}
   ```
   
   ```main.html```:
   
   ```html
   <a href="{% url 'main:create_product' %}">
     <button>Add New Product</button>
   </a>
   <a href="{% url 'main:login' %}">
     <button>Logout</button>
   </a>
   ```
5. Menambahkan decorator  ```login_required``` di ```views.py``` pada ```show_main``` sebagai laman utama untuk autentikasi login, yaitu mengharuskan login dulu untuk mengaksesnya. 
   ```python
   from django.contrib.auth.decorators import login_required

   @login_required(login_url='/login')
   def show_main(request):
   ```
6. Menerapkan cookies untuk menyimpan data user saat login pada beberapa fungsi di ```views.py```. Sebelumnya mengimport beberapa yang dibutuhkan seperti HttpResponseRedirect, reverse, dan datetime.
   ```python
   def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'npm': '2306165553',
        'products': products,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)
   
   ...
   def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
   ```
7. Menghubungan model ```Product``` dengan``` user``` menggunakan field `ForeignKey` yang merujuk ke model `User`
      ```python
      from django.contrib.auth.models import User

      class Product(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)
      ```
8. Melakukan migrasi database menggunakan ```python manage.py makemigrations``` dan ```python manage.py migrate```

## Tugas 5

### 1. Urutan prioritas CSS selector

Dalam CSS, urutan prioritas selector disebut juga sebagai "specificity" (spesifisitas). Urutannya dari yang paling tinggi ke paling rendah:
1. Inline styles (style yang ditulis langsung pada elemen HTML)
2. ID selectors (#id)
3. Class selectors (.class), attribute selectors ([attr]), dan pseudo-classes (:hover)
4. Element selectors (p, div, span, dll) dan pseudo-elements (::before, ::after)
Jika ada konflik antara selector, yang lebih spesifik akan digunakan. Jika spesifisitasnya sama, selector yang ditulis terakhir akan digunakan.

### 2. Pentingnya responsive design

Responsive design sangat penting karena beberapa hal berikut.

- Pengguna mengakses web dari berbagai perangkat (desktop, tablet, smartphone)
- Meningkatkan pengalaman pengguna di semua perangkat
- Membantu SEO karena Google lebih menyukai situs yang mobile-friendly
- Lebih efisien daripada membuat versi terpisah untuk desktop dan mobile

Contoh aplikasi yang menerapkan responsive design adalah https://x.com/

Contoh aplikasi yang belum menerapkan responsive design https://www.headhunterhairstyling.com/

### 3. Perbedaan margin, border, dan padding:

- Margin: Ruang di luar elemen, memisahkan elemen dari elemen lain
- Border: Garis di sekeliling elemen, berada di antara margin dan padding
- Padding: Ruang di dalam elemen, antara konten dan border

#### Implementasi CSS
##### vanilla css (biasa)
```css
.kotak {
  margin: 10px;        /* Jarak 10px ke semua arah */
  border: 2px solid black;  /* Garis tebal 2px, solid, warna hitam */
  padding: 15px;       /* Jarak dalam 15px ke semua arah */
}
```
##### tailwind
- Margin: m-[nilai] (contoh: m-4 untuk margin di semua sisi)
- Border: border-[ketebalan] (contoh: border-2 untuk border 2px)
- Padding: p-[nilai] (contoh: p-4 untuk padding di semua sisi)

### 4. Konsep flexbox dan grid layout

#### Flexbox
- Digunakan untuk layout satu dimensi (baris atau kolom).
- Sangat baik untuk mengatur item dalam container.
- Mudah untuk membuat layout yang responsif dan mengatur alignment.
- Ideal untuk komponen UI seperti navbar, card layouts, atau form inputs.

#### Kegunaan Flexbox
- Vertical centering
- Equal height columns
- Distribusi ruang antar item
- Reordering elemen tanpa mengubah HTML

##### Implementasi dasar flexbox
css biasa:
```css
.container {
  display: flex;
  flex-direction: row; /* atau column */
  justify-content: center; /* horizontal alignment */
  align-items: center; /* vertical alignment */
}

.item {
  flex: 1; /* item akan mengambil ruang yang tersedia secara merata */
}
```

tailwind:

- flex: untuk membuat container flexbox
- flex-row atau flex-col: untuk menentukan arah flex
- justify-center: untuk mengatur align horizontal
- items-center: untuk mengatur align vertikal

```html
<div class="flex justify-between items-center">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

#### Grid Layout
- Digunakan untuk layout dua dimensi (baris dan kolom sekaligus).
- Ideal untuk layout halaman keseluruhan atau section yang kompleks.
- Memungkinkan kontrol yang lebih presisi atas penempatan item.
- Sangat berguna untuk desain yang membutuhkan alignment vertikal dan horizontal.

#### Kegunaan Grid
- Membuat layout kompleks dengan mudah
- Responsive design tanpa media queries
- Overlap elemen
- Membuat grid asimetris

#### Implementasi dasar grid

css biasa:
```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 kolom dengan lebar yang sama */
  gap: 20px; /* Jarak antar item */
}

.item {
  grid-column: span 2; /* Item akan mengambil 2 kolom */
}
```

tailwind:
- grid: untuk membuat container grid
- grid-cols-[jumlah]: untuk menentukan jumlah kolom
- gap-[nilai]: untuk memberi jarak antar item grid

```html
<div class="grid grid-cols-3 gap-4">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
    <div>Item 4</div>
    <div>Item 5</div>
    <div>Item 6</div>
</div>
```
### Langkah-langkah 
1. Konfigurasi tailwind dengan mengubah ```base.html```.
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
       <script src="https://cdn.tailwindcss.com"></script>
       <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
     </head>
     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```
2. Membuat fungsi views baru.
   ```python
   def about(request):
       return render(request, "about.html")
   
   def edit_product(request, id):
       product = Product.objects.get(pk = id)
       form = ProductForm(request.POST or None, instance=product)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "edit_product.html", context)
   
   def delete_product(request, id):
       product = Product.objects.get(pk = id)
       product.delete()
       return HttpResponseRedirect(reverse('main:show_main'))
   ```
3. Routing fungsi tersebut ke urls.py di main
   ```python
   urlpatterns = [
       ...
       path('edit_product/<uuid:id>/', edit_product, name='edit_product'),
       path('delete_product/<uuid:id>/', delete_product, name='delete_product'),
       path('about/', about, name='about'),
   ]
   ```
4. Membuat direktori static pada direktori utama untuk meenyimpan file statis.
5. Membuat file global.css dan menambahkan gambar yang diperlukan pada direktori tersebut.
6. Membuat Navbar.html untuk tampilan navigasi pada direktori templates di direktori utama.
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Responsive Navbar</title>
     <script src="https://cdn.tailwindcss.com"></script>
   </head>
   <body class="bg-gray-100">
   
     <!-- Navbar -->
     <nav class="bg-slate-950 shadow-lg sticky top-0 z-50">
       <div class="max-w-7xl mx-auto px-4">
         <div class="flex justify-between items-center">
           <div class="flex space-x-4">
             <div>
               <a href="{% url 'main:show_main' %}" class="flex items-center py-5 px-2 text-white transition duration-500 transform hover:scale-110">
                 <span class="font-bold text-xl">Booktique</span>
               </a>
             </div>
             <div class="hidden md:flex items-center space-x-1">
               <a href="{% url 'main:about' %}" class="py-5 px-3 text-white hover:text-gray-300 transition-transform duration-300 hover:scale-110">About</a>
               <a href="{% url 'main:show_main' %}" class="py-5 px-3 text-white hover:text-gray-300 transition-transform duration-300 hover:scale-110">Products</a>
             </div>
           </div>
   
           <!-- Search Form -->
           <form method="GET" action="{% url 'main:show_main' %}" class="flex items-center">
             <input type="text" name="query" placeholder="Search products..." class="border rounded-full px-2 py-1 transition duration-500 transform hover:shadow-md focus:ring-2 focus:ring-blue-800 focus:outline-none" />
             <button type="submit" class="ml-2 py-1 px-3 bg-blue-800 text-white rounded-full hover:bg-blue-950 transition duration-300 hover:shadow-lg">
               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35m1.35-5.65a7 7 0 11-14 0 7 7 0 0114 0z"></path>
               </svg>
             </button>
           </form>
   
           <div class="md:flex items-center space-x-4 hidden">
             {% if user.is_authenticated %}
               <div class="text-white">Welcome, {{ user.username }}!</div>
               <a href="{% url 'main:logout' %}" class="py-2 px-4 text-white bg-red-900 hover:bg-red-700 transition duration-300 rounded-full">Logout</a>
             {% else %}
               <a href="{% url 'main:login' %}" class="py-2 px-4 text-white bg-blue-900 hover:bg-blue-950 transition duration-300 rounded-full">Login</a>
               <a href="{% url 'main:register' %}" class="py-2 px-4 text-white bg-green-800 hover:bg-green-900 transition duration-300 rounded-full">Register</a>
             {% endif %}
           </div>
   
           <div class="md:hidden flex items-center">
             <button id="hamburger" class="mobile-menu-button">
               <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                 <path d="M4 6h16M4 12h16M4 18h16"></path>
               </svg>
             </button>
           </div>
         </div>
       </div>
     </nav>
   
     <!-- Mobile Menu -->
     <div class="mobile-menu fixed inset-x-0 z-50 hidden bg-white shadow-lg transition-transform duration-300 transform -translate-y-full" id="mobileMenu">
       <div class="flex flex-col h-full">
         <div class="flex items-center justify-between p-4">
           <span class="font-bold">Menu</span>
           <button id="close-menu" class="text-gray-700 focus:outline-none">
             <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
             </svg>
           </button>
         </div>
         <div class="flex-1 overflow-y-auto">
           <div class="flex flex-col items-center">
             <a href="{% url 'main:about' %}" class="block w-full py-2 px-4 text-sm text-gray-700 hover:bg-gray-200 transition duration-300 text-center">About</a>
             <a href="{% url 'main:show_main' %}" class="block w-full py-2 px-4 text-sm text-gray-700 hover:bg-gray-200 transition duration-300 text-center">Products</a>
           </div>
   
           <div class="border-t border-gray-200 mt-2"></div> <!-- Separator -->
   
           <div class="flex flex-col items-center px-4 py-2">
             {% if user.is_authenticated %}
               <div class="text-sm text-gray-700 mb-2 text-center w-full bg-blue-100 rounded-full p-2">
                 <span class="font-bold text-blue-800">Welcome, {{ user.username }}!</span>
               </div>
               <a href="{% url 'main:logout' %}" class="block w-full py-2 px-4 text-sm text-center bg-red-900 text-white hover:bg-red-700 transition duration-300 rounded-full">Logout</a>
             {% else %}
               <a href="{% url 'main:login' %}" class="block w-full py-2 px-4 text-sm text-center bg-blue-900 text-white hover:bg-blue-950 transition duration-300 rounded-full mb-2">Login</a>
               <a href="{% url 'main:register' %}" class="block w-full py-2 px-4 text-sm text-center bg-green-800 text-white hover:bg-green-900 transition duration-300 rounded-full">Register</a>
             {% endif %}
           </div>
         </div>
       </div>
     </div>
   
     <script>
       const hamburger = document.getElementById('hamburger');
       const closeMenu = document.getElementById('close-menu');
       const mobileMenu = document.getElementById('mobileMenu');
   
       hamburger.addEventListener('click', () => {
         mobileMenu.classList.remove('hidden');
         mobileMenu.classList.remove('-translate-y-full');
       });
   
       closeMenu.addEventListener('click', () => {
         mobileMenu.classList.add('-translate-y-full');
         mobileMenu.classList.add('hidden');
       });
     </script>
   
   </body>
   </html>
   ```
8. Menambahkan file-file html baru yang berkorespondensi dengan fungsi fungsi views yang dibuat tadi.
   ```about.html```
   ```html
   {% extends 'base.html' %}
   {% block meta %}
   <title>Booktique - About</title>
   {% endblock meta %}
   
   {% block content %}
   {% include 'navbar.html' %}
   <!-- Hero Section -->
   <section class="bg-blue-200 text-blue-950 py-20">
       <div class="max-w-4xl mx-auto text-center">
           <h1 class="text-4xl font-bold mb-4 animate-bounce">Welcome to Booktique!</h1>
           <p class="mb-6 text-lg">Your one-stop e-commerce platform for all things books.</p>
           <a href="{% url 'main:show_main' %}">
               <button class="py-2 px-4 bg-blue-950 text-white rounded-full hover:bg-slate-950 transition transform hover:scale-105">
                   View Products
               </button>
           </a>
       </div>
   </section>
   
   <!-- About and Contact Section -->
   <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-6 p-6">
       <!-- About Us Card -->
       <div class="bg-white rounded-lg shadow-md transition-transform transform hover:scale-105 p-4">
           <h2 class="mt-6 text-lg font-semibold">About Us</h2>
           <p id="about-text" class="mt-2 overflow-hidden max-h-20 text-ellipsis cursor-pointer" onclick="toggleAboutModal()">At Booktique, we are passionate about connecting book lovers with their next great read. 
              Whether you’re searching for bestsellers, rare finds, or just looking to explore, we have something for everyone!</p>
           <button class="text-blue-600 hover:underline mt-2" onclick="toggleAboutModal()">Show More</button>
       </div>
   
       <!-- Contact Us Card -->
       <div class="bg-white rounded-lg shadow-md transition-transform transform hover:scale-105 p-4">
           <h2 class="mt-6 text-lg font-semibold">Contact Us</h2>
           <p class="mt-2 overflow-hidden max-h-20 text-ellipsis">We would love to hear from you! Feel free to reach out with any questions or feedback.</p>
           <ul class="mt-2">
               <li>Email: <a href="mailto:info@booktique.com" class="text-blue-600 hover:underline">info@booktique.com</a></li>
               <li>Phone: <a href="tel:+62234567890" class="text-blue-600 hover:underline">+62 (234) 567-890</a></li>
           </ul>
       </div>
   </div>
   
   <!-- Modal About Us -->
   <div id="about-modal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 hidden">
       <div class="bg-white rounded-lg p-6 max-w-md mx-auto">
           <h2 class="text-lg font-semibold">About Us</h2>
           <p class="mt-2">At Booktique, we are passionate about connecting book lovers with their next great read. 
              Whether you’re searching for bestsellers, rare finds, or just looking to explore, we have something for everyone!</p>
           <button class="mt-4 py-2 px-4 bg-blue-950 text-white rounded hover:bg-blue-700" onclick="toggleAboutModal()">Close</button>
       </div>
   </div>
   
   <!-- Social Media Section -->
   <div class="max-w-4xl mx-auto p-6 bg-slate-950 rounded-lg shadow-md mt-6 text-center transition-transform transform hover:scale-105">
       <h2 class="mt-6 text-white text-lg font-semibold">Follow Us</h2>
       <div class="flex justify-center space-x-4 mt-2">
           <a href="https://instagram.com/" class="text-white hover:underline transition duration-300">Instagram</a>
           <a href="https://facebook.com/" class="text-white hover:underline transition duration-300">Facebook</a>
           <a href="https://twitter.com/" class="text-white hover:underline transition duration-300">Twitter</a>
       </div>
   </div>
   
   <script>
       function toggleAboutModal() {
           const modal = document.getElementById('about-modal');
           modal.classList.toggle('hidden');
       }
   </script>
   
   {% endblock content %}
   ```
   
   ```edit_product.html```
   ```html
   {% extends 'base.html' %}
   {% load static %}
   
   {% block meta %}
   <title>Edit Product - Booktique</title>
   {% endblock meta %}
   
   {% block content %}
   {% include 'navbar.html' %}
   <div class="flex flex-col min-h-screen bg-gray-100">
     <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
       <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product</h1>
     
       <div class="bg-white rounded-lg p-6 form-style">
         <form method="POST" class="space-y-6">
             {% csrf_token %}
             {% for field in form %}
                 <div class="flex flex-col">
                     <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                         {{ field.label }}
                     </label>
                     <div class="w-full">
                         {{ field }}
                     </div>
                     {% if field.help_text %}
                         <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                     {% endif %}
                     {% for error in field.errors %}
                         <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                     {% endfor %}
                 </div>
             {% endfor %}
           <div class="flex justify-center mt-6">
               <button type="submit" class="text-white font-semibold px-6 py-3 rounded-lg transition duration-300 ease-in-out w-full bg-blue-950 hover:bg-slate-900">
                   Update Product
               </button>
           </div>
         </form>
     </div>
   
     <div class="flex justify-center mt-4">
         <a href="{% url 'main:show_main' %}" class="bg-gray-600 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out">
             Back to Product List
         </a>
     </div>
     </div>
   </div>
   {% endblock content %}
   ```
9. Membuat file html card yang akan ditampilkan di main.

      ```card_product.html```
      ```html
      <div class="flex flex-wrap justify-center">
          <!-- Product Card -->
          <div class="relative break-inside-avoid w-full h-full sp-6 animate-fadeIn">
              <div class="relative top-5 bg-white shadow-md rounded-2xl mb-6 break-inside-avoid flex flex-col border-2 border-gray-300 transition-transform duration-300 h-full hover:scale-105">
                  <!-- Product Information -->
                  <div class="bg-blue-100 text-gray-800 p-4 rounded-t-2xl border-b-2 border-gray-300 flex flex-col flex-grow">
                      <h3 class="font-bold text-center text-2xl mb-1">{{ product.name }}</h3>
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" viewBox="0 0 20 20" fill="currentColor">
                              <path d="M10 3a7 7 0 100 14 7 7 0 000-14zM1 17a9 9 0 0118 0H1z" />
                          </svg>
                          <p class="text-gray-600 ml-2">{{ product.author }}</p>
                      </div>
                  </div>
      
                  <!-- Product Stock and Price -->
                  <div class="p-4 flex-grow">
                      <div class="grid grid-cols-2 gap-4">
                          <div class="flex flex-col items-center">
                              <span class="text-gray-600 text-sm font-bold text-center">Stock</span>
                              <span class="inline-block bg-green-200 text-green-800 text-lg font-medium px-2.5 py-0.5 rounded-full flex-grow text-center">
                                  {{ product.stock_quantity }}
                              </span>
                          </div>
                          <div class="flex flex-col items-center">
                              <span class="text-gray-600 text-sm font-bold text-center">Price</span>
                              <span class="inline-block bg-yellow-200 text-yellow-800 text-lg font-medium px-2.5 py-0.5 rounded-full flex-grow text-center">
                                  ${{ product.price }}
                              </span>
                          </div>
                      </div>
      
                      <!-- Product Description -->
                      <p class="mt-4 text-gray-700 overflow-hidden text-ellipsis" style="max-height: 50px; overflow: hidden;">
                          {{ product.description }}
                      </p>
      
                      <!-- Show More Button -->
                      <button type="button" class="mt-4 text-blue-600 hover:underline" onclick="showDescriptionModal(this)" data-name="{{ product.name }}" data-author="{{ product.author }}" data-stock="{{ product.stock_quantity }}" data-price="{{ product.price }}" data-description="{{ product.description }}">
                          Show More
                      </button>
                  </div>
      
                  <!-- Edit & Delete Buttons -->
                  <div class="flex justify-center p-4 space-x-4 border-t-2 border-gray-300">
                      <a href="{% url 'main:edit_product' product.id %}" class="bg-blue-950 hover:bg-slate-900 text-white rounded-lg p-2 transition duration-300 flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                              <path d="M12.586 2.586a2 2 0 012.828 2.828l-8 8a1 1 0 01-.293.207l-3 1a1 1 0 01-1.207-1.207l1-3a1 1 0 01.207-.293l8-8z" />
                          </svg>
                          <span class="ml-1">Edit</span>
                      </a>
                      <a href="{% url 'main:delete_product' product.id %}" class="bg-red-900 hover:bg-red-950 text-white rounded-lg p-2 transition duration-300 flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                              <path fill-rule="evenodd" d="M4 4a1 1 0 011-1h10a1 1 0 011 1v1H4V4zM4 6h12v12a2 2 0 01-2 2H6a2 2 0 01-2-2V6z" clip-rule="evenodd" />
                          </svg>
                          <span class="ml-1">Delete</span>
                      </a>
                  </div>
              </div>
          </div>
      </div>
      
      <!-- Modal Product Details -->
      <div id="description-modal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 hidden z-50">
          <div class="bg-white rounded-lg p-6 max-w-md w-full mx-auto overflow-hidden" style="max-height: 80vh; overflow-y: auto;">
              <!-- Product Information Modal -->
              <h3 class="font-bold text-2xl mb-1"></h3>
              <div class="flex items-center mb-4">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M10 3a7 7 0 100 14 7 7 0 000-14zM1 17a9 9 0 0118 0H1z" />
                  </svg>
                  <p class="text-gray-600 ml-2 modal-author"></p>
              </div>
      
              <!-- Stock & Price Modal -->
              <div class="grid grid-cols-2 gap-4 mb-4">
                  <div class="flex flex-col items-center">
                      <span class="text-gray-600 text-sm font-bold text-center">Stock</span>
                      <span class="inline-block bg-green-200 text-green-800 text-lg font-medium px-2.5 py-0.5 rounded-full flex-grow text-center modal-stock"></span>
                  </div>
                  <div class="flex flex-col items-center">
                      <span class="text-gray-600 text-sm font-bold text-center">Price</span>
                      <span class="inline-block bg-yellow-200 text-yellow-800 text-lg font-medium px-2.5 py-0.5 rounded-full flex-grow text-center modal-price"></span>
                  </div>
              </div>
      
              <!-- Description with Scroll -->
              <div class="overflow-auto max-h-[300px] mb-4">
                  <p class="text-gray-700 modal-description"></p>
              </div>
      
              <!-- Edit & Delete Buttons  -->
              <div class="flex justify-center space-x-4 mb-4 border-t-2 border-gray-300 pt-4">
                  <a href="{% url 'main:edit_product' product.id %}" class="bg-blue-950 hover:bg-slate-900 text-white rounded-lg px-4 py-2 transition duration-300 flex items-center">
                      Edit
                  </a>
                  <a href="{% url 'main:delete_product' product.id %}" class="bg-red-900 text-white rounded-lg px-4 py-2">
                      Delete
                  </a>
              </div>
      
              <!-- Close Button -->
              <button class="py-2 px-4 bg-gray-600 text-white rounded hover:bg-gray-800 w-full" onclick="hideDescriptionModal()">Close</button>
          </div>
      </div>
      
      <script>
          function showDescriptionModal(button) {
              const modal = document.getElementById('description-modal');
              
              // Get data from button attributes
              const name = button.getAttribute('data-name');
              const author = button.getAttribute('data-author');
              const stock = button.getAttribute('data-stock');
              const price = button.getAttribute('data-price');
              const description = button.getAttribute('data-description');
              
              // Update modal content
              modal.querySelector('h3').textContent = name;
              modal.querySelector('.modal-author').textContent = author;
              modal.querySelector('.modal-stock').textContent = stock;
              modal.querySelector('.modal-price').textContent = `$${price}`;
              modal.querySelector('.modal-description').textContent = description;
              
              // Show modal
              modal.classList.remove('hidden');
          }
      
          function hideDescriptionModal() {
              document.getElementById('description-modal').classList.add('hidden');
          }
      </script>
      
      <style>
          @keyframes fadeIn {
              from {
                  opacity: 0;
              }
              to {
                  opacity: 1;
              }
          }
      
          .animate-fadeIn {
              animation: fadeIn 1s ease-in-out;
          }
      </style>
      ```
      
      ```card_info.html```
      ```html
      {% load static %}
      <div class="relative break-inside-avoid w-full max-w-lg mx-auto">
          <div class="bg-blue-100 shadow-lg rounded-2xl mb-6 p-8 border-2 border-transparent transition-transform duration-300 transform hover:scale-105">
              <div class="flex items-center mb-4">
                  <div class="h-20 w-20 flex items-center justify-center bg-white rounded-full mr-4">
                      <img src="{% static 'image/photo_profile.jpg' %}" alt="Profile Image" class="h-20 w-20 rounded-full object-cover">
                  </div>
                  <div>
                      <h3 class="font-bold text-3xl text-blue-950">{{ name }}</h3>
                      <p class="text-blue-950">{{ npm }}</p>
                  </div>
              </div>
              <div class="grid grid-cols-2 gap-4">
                  <div class="flex flex-col items-center">
                      <span class="text-blue-950 text-sm font-bold mb-2">Class</span> 
                      <span class="bg-white text-blue-950 text-lg font-medium px-3 py-1 rounded-2xl">
                          {{ class }}
                      </span>
                  </div>
                  <div class="flex flex-col items-center">
                      <span class="text-blue-950 text-sm font-bold mb-2">Last Login</span> 
                      <span class="bg-white text-blue-950 text-lg font-medium px-3 py-1 rounded-2xl">
                          {{ last_login }}
                      </span>
                  </div>
              </div>
          </div>
      </div>
      
      ```
10. Modifikasi file file html yang sudah dibuat sebelumnya dengan css untuk mempercantik tampilan.
    
      ```login.html```
      ```html
      {% extends 'base.html' %}
      
      {% block meta %}
      <title>Login</title>
      {% endblock meta %}
      
      {% block content %}
      {% include 'navbar.html' %}
      <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
          <div>
            <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
              Login to your account
            </h2>
          </div>
          <form class="mt-8 space-y-6" method="POST" action="">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
              <div>
                <label for="username" class="sr-only">Username</label>
                <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-950 focus:border-blue-950 focus:z-10 sm:text-sm" placeholder="Username">
              </div>
              <div>
                <label for="password" class="sr-only">Password</label>
                <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-950 focus:border-blue-950 focus:z-10 sm:text-sm" placeholder="Password">
              </div>
            </div>
      
            <div>
              <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-950 hover:bg-slate-950 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-950">
                Sign in
              </button>
            </div>
          </form>
      
          {% if messages %}
          <div class="mt-4">
            {% for message in messages %}
            {% if message.tags == "success" %}
                  <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                  </div>
              {% elif message.tags == "error" %}
                  <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                  </div>
              {% else %}
                  <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                  </div>
              {% endif %}
            {% endfor %}
          </div>
          {% endif %}
      
          <div class="text-center mt-4">
            <p class="text-sm text-black">
              Don't have an account yet?
              <a href="{% url 'main:register' %}" class="font-medium text-blue-500 hover:text-blue-700">
                Register Now
              </a>
            </p>
          </div>
        </div>
      </div>
      {% endblock content %}
      ```
      
      ```register.html```
      ```html
      {% extends 'base.html' %}
      
      {% block meta %}
      <title>Register</title>
      {% endblock meta %}
      
      {% block content %}
      <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8 form-style">
          <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
              Create your account
            </h2>
          </div>
          <form class="mt-8 space-y-6" method="POST">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
              {% for field in form %}
                <div class="{% if not forloop.first %}mt-4{% endif %}">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                    {{ field.label }}
                  </label>
                  <div class="relative">
                    {{ field }}
                    <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                      {% if field.errors %}
                        <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                      {% endif %}
                    </div>
                  </div>
                  {% if field.errors %}
                    {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                  {% endif %}
                </div>
              {% endfor %}
            </div>
      
            <div>
              <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-950 hover:bg-slate-950 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-950">
                Register
              </button>
            </div>
          </form>
      
          {% if messages %}
          <div class="mt-4">
            {% for message in messages %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
            </div>
            {% endfor %}
          </div>
          {% endif %}
      
          <div class="text-center mt-4">
            <p class="text-sm text-black">
              Already have an account?
              <a href="{% url 'main:login' %}" class="font-medium text-blue-500 hover:text-blue-700">
                Login here
              </a>
            </p>
          </div>
        </div>
      </div>
      {% endblock content %}
      ```
      
      ```create_product.html```
      ```html
      {% extends 'base.html' %}
      {% load static %}
      
      {% block meta %}
      <title>Add New Product - Booktique</title>
      {% endblock meta %}
      
      {% block content %}
      {% include 'navbar.html' %}
      <div class="flex flex-col min-h-screen bg-gray-100">
        <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
          <h1 class="text-3xl font-bold text-center mb-8 text-black">Add New Product</h1>
        
          <div class="bg-white rounded-lg p-6 form-style">
            <form method="POST" class="space-y-6">
                {% csrf_token %}
                {% for field in form %}
                    <div class="flex flex-col">
                        <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                            {{ field.label }}
                        </label>
                        <div class="w-full">
                            {{ field }}
                        </div>
                        {% if field.help_text %}
                            <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                        {% endif %}
                        {% for error in field.errors %}
                            <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                        {% endfor %}
                    </div>
                {% endfor %}
                <div class="flex justify-center mt-6">
                  <button type="submit" class="text-white font-semibold px-6 py-3 rounded-lg transition duration-300 ease-in-out w-full bg-blue-950 hover:bg-slate-950">
                      Add Product
                  </button>
              </div>
            </form>
        </div>
      
        <div class="flex justify-center mt-4">
            <a href="{% url 'main:show_main' %}" class="bg-gray-600 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out">
                Back to Product List
            </a>
        </div>
        </div>
      </div>
      {% endblock content %}
      
      ```
      
      ```main.html```
      ```html
      {% extends 'base.html' %}
      
      {% load static %}
      
      {% block meta %}
      <title>Booktique - Product List</title>
      {% endblock meta %}
      
      {% block content %}
      {% include 'navbar.html' %}
      <div class="container mx-auto p-6">
      
          <!-- ID Card -->
          <div class="grid grid-cols-1 gap-6 mb-6">
              {% include "card_info.html" with name=name npm=npm class=class last_login=last_login %}
          </div>
      
          <div class="flex flex-col md:flex-row justify-between items-center mb-6">
              <!-- Sort dropdown & button -->
              <form method="get" action="" class="flex flex-col md:flex-row items-center mb-4 md:mb-0">
                  <label for="sort-field" class="mr-2">Sort By</label>
                  <select id="sort-field" name="sort" class="border border-gray-300 rounded-lg p-2 mb-2 md:mb-0 md:mr-4" required>
                      <option value="">Select</option>
                      <option value="name">Name</option>
                      <option value="price">Price</option>
                      <option value="stock">Stock</option>
                  </select>
              
                  <label for="sort-order" class="ml-4 mr-2">Order</label>
                  <select id="sort-order" name="order" class="border border-gray-300 rounded-lg p-2 mb-2 md:mb-0" required>
                      <option value="">Select</option>
                      <option value="asc">Ascending</option>
                      <option value="desc">Descending</option>
                  </select>
              
                  <button type="submit" class="ml-4 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out bg-blue-950 hover:bg-slate-900">
                      Sort
                  </button>
              </form>
              
      
              <a href="{% url 'main:create_product' %}" class="text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out bg-blue-950 hover:bg-slate-900">
                  Add New Product
              </a>
          </div>
      
          <!-- product card -->
          {% if not products %}
              <div class="flex flex-col items-center justify-center">
                  <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-24 h-24 mb-2"/>
                  <p>No products available in Booktique :[ </p>
              </div>
          {% else %}
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
              {% for product in products %}
                  <div class="flex justify-center"> 
                      {% include 'card_product.html' with product=product %}
                  </div>
              {% endfor %}
          </div>
          {% endif %}
          
      {% endblock content %}
      ```

   

   
    









    
     
