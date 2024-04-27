from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact_form/contact.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here you can save the form data to a database, send an email, etc.
            # For simplicity, let's just print the data to the console
            print(f"Name: {name}, Email: {email}, Message: {message}")
            # Optionally, you can redirect the user to a success page
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')