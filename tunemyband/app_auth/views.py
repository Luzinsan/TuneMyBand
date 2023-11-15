from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# from .forms import UserProfileForm


# class UserProfileCreateView(CreateView):
#     template_name = 'home/sign_up.html'
#     form_class = UserProfileForm
#     success_url = reverse_lazy('home/home.html')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['rubrics'] = Rubric.objects.all()
#         return context


def sign_in(request):
    return render(request, 'home/sign_in.html', {})


# def sign_up(request):
#     return render(request, 'home/sign_up.html', {})

