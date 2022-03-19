from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import DataEntry


class DataEntryForm(forms.ModelForm):
    class Meta:
        model = DataEntry
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'branch_code')

    def __init__(self, *args, **kwargs):
        group_input = kwargs.pop('group_input', None)
        new_list = [(item.get('branch_code'), item.get('branch_code')) for item in list(DataEntry.objects.all().values())]
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['branch_code'].widget = forms.Select(
            choices=new_list)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'branch_code')
