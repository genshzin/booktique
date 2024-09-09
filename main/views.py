from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Booktique',
        'name': 'Nasha Zahira',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
