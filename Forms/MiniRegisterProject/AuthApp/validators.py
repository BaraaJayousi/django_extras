from django.core.exceptions import ValidationError
import re

def validate_password_match(password, confirm_password):
  if password != confirm_password:
    raise ValidationError(
      f"Passwords do not match"
    )
  
# vlidates inputed password if it is between 8 - 16 characters and it has special character and a digit a small letter and a capital latter
def password_pattern_validator(value):
  pattern = re.compile("^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$")
  if not pattern.match(value):
    raise ValidationError(
      f"The provided password should be 8 characters long and has 1 special character"
    )
  
def  check_unique_email(custom_model, email):
  if custom_model.objects.filter(email=email).first():
    raise ValidationError(
      f"The email: {email} is already used, please use a different email"
    )
  

def validate_user_login(model, email, password):
  if not model.objects.login(email,password):
    raise ValidationError(
      f"Your email or password doesn't match our records"
    )