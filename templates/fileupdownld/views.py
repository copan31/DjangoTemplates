from django.shortcuts import render
from .forms import FileUpLdForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import mimetypes
import shutil
from django.http import HttpResponse
import os

# Create your views here.
def index(request):

    if request.method == "POST":
        # POSTデータ取得
        upfile = request.FILES['upfile']

        # 保存
        fileobject = FileSystemStorage()
        filepath = os.path.join(settings.MEDIA_ROOT, upfile.name)
        fileobject.save(filepath, upfile )

        # 変換

        # 変換結果リターン

        # ファイル名からmimetypeを推測。拡張子がないファイル等は、application/octet-stream
        response = HttpResponse(content_type=mimetypes.guess_type(upfile.name)[0] or 'application/octet-stream')
        # Content-Dispositionでダウンロードの強制
        response['Content-Disposition'] = f'attachment; filename={upfile.name}'
        # HttpResponseに、ファイルの内容を書き込む
        shutil.copyfileobj(upfile, response)
        
        return response

    else :
        context = {} 
        context['form'] = FileUpLdForm() 
        return render( request, "index.html", context) 