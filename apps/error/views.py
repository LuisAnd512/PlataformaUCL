from django.shortcuts import render

def error_404(request, *args, **argv):
   return render(request,'shared/error/404.html', status=404)

def error_500(request, *args, **argv):
   return render(request,'shared/error/500.html', status=500)

def error_403(request, *args, **argv):
   return render(request,'shared/error/403.html', status=403)

def error_400(request, *args, **argv):
   return render(request,'shared/error/400.html', status=400)
