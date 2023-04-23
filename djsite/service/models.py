from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Атауы")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Сипаттамасы")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.IntegerField(verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Қызмет'
        verbose_name_plural = 'Қызметтер'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'