from django.shortcuts import render, redirect
from pizza.forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def index(request):
	form = ContactForm(request.POST)

	if request.method == 'POST':
		
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject,message, email, ['admin@admin.py'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('pizza/index')

	return render(request, "pizza/index.html", {'form' : form})