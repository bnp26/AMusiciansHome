from django.conf import settings

settings.configure()

from forms import RegistrationForm

user = {}
user['first_name'] = "Diane"
user['last_name'] = "Lavine"
user['username'] = "dlavine"
user['email'] = "dlavine@gmail.com"
user['phone_num'] = "2162223333"
user['password1'] = "abc12345"
user['password2'] = "abc12345"
form = RegistrationForm(instance=user)
print form