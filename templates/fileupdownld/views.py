from django.shortcuts import render
from .forms import FileUpLdForm, ConfirmForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import mimetypes
import shutil
from django.http import HttpResponse
import os

# Create your views here.
def index(request):

    if request.method == "POST" and request.FILES: # ファイルアップロード
        # POSTデータ取得
        upfile = request.FILES['upfile']

        # 保存
        fileobject = FileSystemStorage()
        filepath = os.path.join(settings.MEDIA_ROOT, upfile.name)
        filename = fileobject.save(filepath, upfile )

        # 確認画面描画
        context = {}
        context['form'] = ConfirmForm(initial = {'filename' : filename})
        return render( request, "confirm.html", context)
   
    elif request.method == "POST":

        # 必要ならfileの内容に変換を加える

        # ファイルオープンして応答
        file_path = request.POST.get("filename")
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                # ファイル名からmimetypeを推測。拡張子がないファイル等は、application/octet-stream
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0] or 'application/octet-stream')
                # Content-Dispositionでダウンロードの強制
                response['Content-Disposition'] = f'attachment; filename={file_path}' 
                return response
        raise "Http404"
    else :
        context = {} 
        context['form'] = FileUpLdForm() 
        return render( request, "index.html", context) 