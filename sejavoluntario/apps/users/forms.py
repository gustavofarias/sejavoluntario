from django import forms

class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput())
    repeat_passwd = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        passwd = cleaned_data.get("passwd")
        repeat_passwd = cleaned_data.get("repeat_passwd")
        if passwd != repeat_passwd:
            raise forms.ValidationError("Passwd and Repeat passwd don't match.")

        return cleaned_data