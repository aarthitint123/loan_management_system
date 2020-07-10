from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm,Application_Form
from .decorators import check_recaptcha

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "lander.html", context)

@check_recaptcha
def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid() and  request.recaptcha_is_valid:
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup1.html", context)


def logout_view(request):
    logout(request)#inbuilt function
    return redirect('/')


def app_view(request):
    next = request.GET.get('next')
    form = Application_Form(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        applicant_name = form.save(commit=False)
        dob = form.cleaned_data.get('dob')
        pan_no = form.cleaned_data.get('pan_no')
        adhaar_no = form.cleaned_data.get('adhaar_no')
        parent_name = form.cleaned_data.get('parent_name')

        parent_occ=form.cleaned_data.get('parent_occ')
        address=form.cleaned_data.get('address')
        institution_name=form.cleaned_data.get('institution_name')
        inst_code=form.cleaned_data.get('inst_code')
        year_of_passing=form.cleaned_data.get('year_of_passing')
        fee=form.cleaned_data.get('fee')
        loanamt=form.cleaned_data.get('loanamt')
        tenure=form.cleaned_data.get('tenure')
        bank_name=form.cleaned_data.get('bank_name')
        acc_no=form.cleaned_data.get('acc_no')
        ifsc=form.cleaned_data.get('ifsc')



        user.save()


        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "app_create.html", context)


