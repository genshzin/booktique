from django.urls import path
from main.views import show_main, about, create_product, edit_product, delete_product
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product/', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete_product/<uuid:id>/', delete_product, name='delete_product'),
    path('about/', about, name='about'),
    path('create_product_ajax/', add_product_ajax, name='add_product_ajax'),
    
]