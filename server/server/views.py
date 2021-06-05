from django.shortcuts import redirect

def render_404(request):
    return redirect("/")
