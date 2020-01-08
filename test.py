def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('join_membership/register_result.html')
        else:
            form = RegisterForm()
        return render(request, 'join_membership/register.html', {'form':form})