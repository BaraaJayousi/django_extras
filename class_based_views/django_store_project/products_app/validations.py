from django.core.exceptions import ValidationError

def validate_product_name_length(value):
  if len(value) < 8:
    raise ValidationError(
      message="Product Name should be at least 8 characters",
      code = "invalid"
    )
  

def validate_product_price(value):
  if value <= 0:
    raise ValidationError(
      message="Product Price should be grater than 0 $",
      code="invalid"
    )
  
def validate_product_description(value):
  if len(value) > 50:
    raise ValidationError(
      message="Product Description should not be more than 50 characters",
      code="invalid"
    )