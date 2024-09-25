from django.shortcuts import render, redirect
from . forms import UserForm
from . models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect




def main_page(request):
    return render(request, 'user/main_page.html')


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('next_step')  # Redirect to a success page or another view
    else:
        form = UserForm()

    return render(request, 'user/create_user.html', {'form': form})



def next_step(request):
    return render(request, 'user/next_step.html')




def show_user(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'user/show_user.html', {'users': users})



def delete_user(request):
    users = User.objects.all()  # Fetch all users
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('delete_user')  # Refresh the page after deletion

    return render(request, 'user/delete_user.html', {'users': users})
def main_page(request):
    return render(request, 'user/main_page.html')