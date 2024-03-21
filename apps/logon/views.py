from django.contrib.auth.views import LoginView
from apps.logon.forms import CustomAuthenticationForm
from django.urls import reverse_lazy



class CustomLoginView(LoginView):
   template_name = 'public/auth/sign_in.html'
   form_class = CustomAuthenticationForm
   
   def form_valid(self, form):
      remember_me = form.cleaned_data['remember_me']
      if not remember_me:
         # Set session expiry to 0 seconds, so it will automatically close after the browser is closed.
         self.request.session.set_expiry(0)
      else:
         # Optionally, you can set a longer expiry time for the session if 'remember_me' is True
         self.request.session.set_expiry(1209600)  # For example, 2 weeks
      return super().form_valid(form)