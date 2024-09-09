# Booktique

Booktique adalah aplikasi web berbasis Django yang dirancang sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform. Proyek ini dibuat oleh Nasha Zahira (2306165553). 
## Tugas 2
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
10. 
   
   
