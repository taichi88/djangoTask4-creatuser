from django.shortcuts import render, redirect
from . forms import UserForm
from . models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ShowUser')  # Redirect to a success page or another view
    else:
        form = UserForm()

    return render(request, 'user/user_template.html', {'form': form})

def show_user(request):
    show_user = User.objects.all()

    return HttpResponse(show_user)



def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == "POST":
        user.delete()
        return redirect('ShowUser')  # Redirect to the view that shows all users after deletion

    return render(request, 'user/confirm_delete.html', {'user': user})