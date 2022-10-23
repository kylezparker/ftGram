from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy


# reverse vs reverse lazy fix

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")
    
    def get_object(self):
        return self.request.user