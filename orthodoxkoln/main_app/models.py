from django.db import models
from django.utils.translation import gettext_lazy as _

class Publication(models.Model):
    title = models.TextField(verbose_name="Заголовок", null=True, blank=True)
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    main_image = models.ImageField(verbose_name="Головне фото", null=True, blank=True,
     upload_to="media/", height_field=None, width_field=None, max_length=None)
    date_created = models.DateField(verbose_name="Дата створення", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"

    def __str__(self):
        return self.title


class PublicationImage(models.Model):
    publication = models.ForeignKey("Publication", verbose_name="Публікація", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Фото", upload_to="media/", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Фото публікації"
        verbose_name_plural = "Фото публікацій"


class PublicationVideo(models.Model):
    publication = models.ForeignKey("Publication", verbose_name="Публікація", on_delete=models.CASCADE)
    video = models.FileField(verbose_name="Відео", upload_to="media/", max_length=255)
    
    class Meta:
        verbose_name = "Відео публікації"
        verbose_name_plural = "Відео публікацій"


class Clergyman(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=50)
    image = models.ImageField(verbose_name="Фото", null=True, blank=True, upload_to="media/", height_field=None, width_field=None, max_length=None)
    job_title = models.CharField(verbose_name="Духовна посада", null=True, blank=True, max_length=255)
    birth_date = models.DateField(verbose_name="Дата народження", null=True, blank=True, auto_now=False, auto_now_add=False)
    deacon_ordination_date = models.DateField(verbose_name="Дияконська хіротонія", null=True, blank=True, auto_now=False, auto_now_add=False)
    priest_ordination_date = models.DateField(verbose_name="Ієрейська хіротонія", null=True, blank=True, auto_now=False, auto_now_add=False)
    secular_education = models.TextField(verbose_name="Світська освіта", null=True, blank=True)
    spiritual_education = models.TextField(verbose_name="Духовна освіта", null=True, blank=True)

    class Meta:
        verbose_name = "Духовенство"
        verbose_name_plural = "Духовенство"

    def __str__(self):
        return self.name


class Parish(models.Model):
    name = models.TextField(verbose_name="Назва", max_length=255)
    main_image = models.ImageField(verbose_name="Головне фото", null=True, blank=True, upload_to="media/", height_field=None, width_field=None, max_length=None)
    address = models.CharField(verbose_name="Адреса", null=True, blank=True, max_length=255)
    date_of_establishment = models.DateField(verbose_name="Дата заснування", null=True, blank=True, auto_now=False, auto_now_add=False)
    history = models.TextField(verbose_name="Історія", null=True, blank=True)

    class Meta:
        verbose_name = "Парафія"
        verbose_name_plural = "Парафії"

    def __str__(self):
        return self.name

class ParishImage(models.Model):
    parish = models.ForeignKey("Parish", verbose_name="Парафія", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Фото", upload_to="media/", height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = "Фото парафії"
        verbose_name_plural = "Фото парафій"


class Calendar(models.Model):
    date = models.DateField(verbose_name="Дата", auto_now=False, auto_now_add=False)
    saints = models.TextField(verbose_name="Пам'ять яких святих")
    day_parable = models.TextField(verbose_name="Притча дня")

    class Meta:
        verbose_name = "Календарний день"
        verbose_name_plural = "Календарні дні"


class Photogallery(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to="media/", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотогалерея"


class Bishop(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    image = models.ImageField(verbose_name="Фото", upload_to=None, height_field=None, width_field=None, max_length=None)
    birth_date = models.DateField(verbose_name="Дата народження", auto_now=False, auto_now_add=False)
    name_day = models.CharField(verbose_name="День тезоіменитства", max_length=20)
    ## Щоб можна було вибирати день і місяць за допомоги метода choices 

    tonsure_date = models.DateField(verbose_name="Дата постригу", auto_now=False, auto_now_add=False)
    deacon_ordination_date = models.DateField(verbose_name="Дата дияконської хіротонії", auto_now=False, auto_now_add=False)
    priest_ordination_date = models.DateField(verbose_name="Дата ієрейської хіротонії", auto_now=False, auto_now_add=False)
    bishop_ordination_date = models.DateField(verbose_name="Дата Архієрейської хіротонії", auto_now=False, auto_now_add=False)
    secular_education = models.TextField(verbose_name="Світська освіта")
    spiritual_education = models.TextField(verbose_name="Духовна освіта")
    biography = models.TextField(verbose_name="Біографія")

    ## Додати def __str__(self):
    ##            return 'Митрополит Онуфрій'
    ## Щоб "Митрополит Онуфрій підтягувалось з бд"

    class Meta:
        verbose_name = "Архієрей"
        verbose_name_plural = "Архієрей"


## Додати def get_absolute_url(self): для кожної моделі