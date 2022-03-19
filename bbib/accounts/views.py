from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import DataEntry
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, HttpResponse
from .forms import DataEntryForm
from django.contrib import messages


def data_entry(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات با موفقیت ثبت شد.', 'success')
            return redirect('home')
    else:
        form = DataEntryForm()
    return render(request, 'data_entry.html', {'form': form})


def get_all_users(request):
    User = get_user_model()
    users = User.objects.all().values()
    return HttpResponse('success')


def result(request):
    if request.user.is_staff:
        all_results = list(DataEntry.objects.all().values())
        return render(request, 'result.html', {'all_results': all_results})
    else:
        User = get_user_model()
        users = User.objects.all().values()
        all_results = []
        for user in users:
            if user.get('branch_code') and (user.get('username') == str(request.user)):
                data_entry_list = list(DataEntry.objects.filter(branch_code=user.get('branch_code')).values())
                for info in data_entry_list:
                    info['value'] = info['value'] / 10
                    all_results.append(info)
        return render(request, 'result.html', {'all_results': all_results})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
