from accounts.models import Application_form
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.http import request

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):  #used for validation purpose
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password: #un and pwd must be filled
            user = authenticate(username=username, password=password)  #returns a object to user
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')

    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'Confirm_password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('Confirm_password')
        if password != password2:
            raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")


        return super(UserRegisterForm, self).clean(*args, **kwargs)


class Application_Form(forms.ModelForm):
    applicant_name = forms.CharField(label='Applicant Name')
    dob = forms.DateField(label="DOB")
    pan_no = forms.IntegerField(label="PAN Number")
    adhaar_no = forms.CharField(label="Adhaar Number")
    parent_name = forms.CharField(label="Parent Name")
    parent_occ=forms.CharField(label="Parent's Occupation")
    address = forms.CharField(label="Residential Address")
    institution_name=forms.CharField(label="Institution Name")
    inst_code = forms.IntegerField(label="Institution Code")
    year_of_passing = forms.DateField(label="Year of passing")
    fee = forms.IntegerField(label="Tution Fee Amount(yearly)")
    loanamt = forms.IntegerField(label="Loan Fee Amount")
    tenure = forms.IntegerField(label="Tenure")
    bank_name=forms.CharField(label="Bank Name")
    ifsc = forms.CharField(label="IFSC CODE")
    acc_no=forms.CharField(label="Bank Account Number")




    class Meta:
        model = Application_form
        fields = [
            'applicant_name',
            'dob',
            'pan_no',
            'adhaar_no',
            'parent_name',
            'parent_occ',
            'address','institution_name','inst_code','year_of_passing','fee','loanamt','tenure','bank_name','acc_no','ifsc',





        ]

    def clean(self, *args, **kwargs):
        applicant_name = self.cleaned_data.get('applicant_name')

        pan_no = self.cleaned_data.get('pan_no')


        return super(Application_Form, self).clean(*args, **kwargs)