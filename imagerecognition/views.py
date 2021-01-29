from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .analysis import detect_labels_local_file

# Create your views here.

def home(request):
  if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        res = detect_labels_local_file('/Users/hongdotcom/Desktop/Sites/django-imgsearch/imgsearch/' + uploaded_file_url)
        print(res)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url,'res': res
        })
  return render(request, 'home.html')

