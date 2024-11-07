from django.forms import ModelForm
from .models import BookInfo
class BookForm(ModelForm):
    class Meta:
        model = BookInfo
        fields = '__all__'