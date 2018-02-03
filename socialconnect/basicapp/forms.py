from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class usercreateform(UserCreationForm):

    class Meta():
        fields=('username','email','password1','password2')
        model=get_user_model()# get_user_model helps to get the models of the user who is currently accessing it.

        def __init__(self,*args,**kwargs):

            super().__init__(*args,**kwargs)
            self.fields['username'].label='Display Name'
            self.fields['email'].label="Email Address"

