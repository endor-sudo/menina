from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
def logout_view(request): 
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))
