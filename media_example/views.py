from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from PIL import Image

def media_example(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            save_path = settings.MEDIA_ROOT / form.cleaned_data["file_upload"] .name
            image = Image.open(fp=form.cleaned_data["file_upload"])
            image.thumbnail((50,50))
            image.save(fp=save_path)

            """
            with open(save_path, 'wb+') as output_file:
                for chunk in form.cleaned_data["file_upload"].chunks():
                    output_file.write(chunk)
            """
    else:
        form = UploadForm()

    return render(request=request, template_name="media-example.html", context={"form": form})

