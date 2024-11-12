from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse, StreamingHttpResponse, Http404

from datetime import datetime, timedelta
import logging

from .models import *
from .forms import *
from .tasks import *
from .utils import *

from selling.settings import EMAIL_HOST_USER

import os
import re 


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log", encoding='utf-8'),  # Задаем кодировку для файла
        logging.StreamHandler()  # Для вывода в консоль
    ]
)

logger = logging.getLogger(__name__)

def home(request):
    title = "Просто школа разработки"

    context ={
        'title': title,
    }

    return render(request, 'main/home.html', context)

def letter(request):
    if request.method == 'POST' :
        try:
            # task_id = request.POST.get('task_id')
            # logger.info(f'task_id: {task_id}')
            fullname    = request.POST.get('fullname')
            his_email   = request.POST.get('email')
            description = request.POST.get('description')

            long_send_order(EMAIL_HOST_USER, fullname, his_email, description)
            long_send_confirmation(fullname, his_email)
            # long_send_student_done_task(task.teacher.email, task.student.name, task_id, task.title)
            # # teacher.task_to_check += 1
            return JsonResponse({'status': 'success', 'refuse': 'add'})
        except Exception as ex:
            logger.error(f'letter Ошибка {ex}')
            return JsonResponse({'status': 'fail'})
    return JsonResponse({'status': 'not post'})
