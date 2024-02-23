from django.shortcuts import render
#from django.conf import settings
from .forms import UploadForm
#from PIL import Image
#from .models import ExampleModel

def media_example(request):
    instance = None
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
    else:
        form = UploadForm()

    return render(request=request, template_name="media-example.html",
                  context={"form": form, "instance": instance})

