from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from main_app.models import *
import logging

# Отримання екземпляра логгера
logger = logging.getLogger(__name__)

# Налаштування рівня журналювання
logger.setLevel(logging.DEBUG)

# Налаштування обробника для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Налаштування формату повідомлень
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Додавання обробника до логгера
logger.addHandler(console_handler)




# def base(request):
#     all_calendar_day = Calendar.objects.all()
#     for calendar_day in all_calendar_day:
#         # logger.debug(calendar_day.date)
#         if (current_date == calendar_day.date):
#             current_calendar_day = calendar_day

#     return render(request,'main/base.html', {'all_calendar_day': all_calendar_day})


all_publication = Publication.objects.all().order_by('-id')
all_calendar_day = Calendar.objects.all()

logger.debug(all_publication)

def main(request):
    paginator = Paginator(all_publication, 5)
    page_number = request.GET.get('page')
    logger.debug(page_number)
    page_obj = paginator.get_page(page_number)
    
    # Працює? Не чіпай!

    p_number = page_obj.number
    actual_page_range = page_obj.paginator.page_range
    visible_page_range = range(int(p_number) - 2, int(p_number) + 3)

    while(min(actual_page_range) > min(visible_page_range)):
        visible_page_range = range(min(visible_page_range) + 1, max(visible_page_range) + 1)

    while(max(actual_page_range) < max(visible_page_range)):
        visible_page_range = range(min(visible_page_range), max(visible_page_range))

    return render(request, 'main_app/main.html', {'page_obj': page_obj, 'visible_page_range': visible_page_range})


def publication(request, publicationid):
    publication_from_db = Publication.objects.get(pk=publicationid)
    publication_images_from_db = publication_from_db.publicationimage_set.all()
    publication_videos_from_db = publication_from_db.publicationvideo_set.all()
    return render(request, 'main_app/publication.html', {'publication_from_db': publication_from_db, 'publication_images_from_db': publication_images_from_db, 'publication_videos_from_db': publication_videos_from_db})


def bishop(request):
    return render(request, 'main_app/bishop.html')


all_parish = Parish.objects.all()

def parishes(request):
    return render(request, 'main_app/parishes.html', {'all_parish': all_parish})


def parish(request, parishid):
    parish_from_db = Parish.objects.get(pk=parishid)
    parish_images_from_db = parish_from_db.parishimage_set.all()
    return render(request, 'main_app/parish.html', {'parish_from_db': parish_from_db, 'parish_images_from_db': parish_images_from_db})


clergymans = Clergyman.objects.all()

def clergy(request):
    return render(request, 'main_app/clergy.html', {'clergymans': clergymans})

def clergyman(request, clergymanid):
    clergyman_from_db = Clergyman.objects.get(pk=clergymanid)
    return render(request, 'main_app/clergyman.html', {'clergyman_from_db': clergyman_from_db})
    

def photogallery(request):
    images_from_db = Photogallery.objects.all()
    return render(request, 'main_app/photogallery.html', {'images_from_db': images_from_db})


def contacts(request):
    return render(request, 'main_app/contacts.html')
