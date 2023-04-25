from django.db import models
from django.contrib.auth.models import AbstractUser
from .utilities import get_timestamp_path
from django.dispatch import Signal

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True,
                                       db_index=True,
                                       verbose_name='Прошел активацию.'
                                       )
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Присылать собщения о новых комментариях?'
                                        )

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass

class Rubric(models.Model):
    name = models.CharField(max_length=20,
                            db_index=True,
                            verbose_name='Название'
                            )
    order = models.SmallIntegerField(default=0,
                                     db_index=True,
                                     verbose_name='Порядок'
                                     )
    super_rubric = models.ForeignKey('SuperRubric',
                                     on_delete=models.PROTECT,
                                     null=True,
                                     blank=True,
                                     verbose_name='Надрубрика'
                                     )

    def __repr__(self):
        return str(self.name), str(self.order), str(self.super_rubric)

    def __str__(self):
        return str(self.name), str(self.order), str(self.super_rubric) #

class SuperRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=True)


class SuperRubric(Rubric):
    objects = SuperRubricManager()


    class Meta:
        proxy = True
        ordering = ('order', 'name') # -> ordering: tuple[str, str] = ('order', 'name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name) # y

class SubRubricManager(models.Manager):
    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=False)

class SubRubric(Rubric):
    objects = SubRubricManager()


    def __repr__(self):
        return '{} {}'.format(str(self.super_rubric.name), str(self.name))


    def __str__(self):
        if self.name is not None:
            return '{}'.format(str(self.name))
        return '{} {}'.format(str(self.super_rubric.name), str(self.name))


    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'


class Bb(models.Model):
    rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=40, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    contacts = models.TextField(verbose_name='Контакты')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор объявления')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


    def __str__(self):
        return '{} {}'.format(str(self.rubric.name), str(self.title))
    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

class AdditionalImage(models.Model):
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE,
                               verbose_name='Объявление')
    image = models.ImageField(upload_to=get_timestamp_path,
                                  verbose_name='Изображение')

    class Meta:
        verbose_name = 'Дополнительная иллюстрация'
        verbose_name_plural = 'Дополнительная иллюстрации'


class Comment(models.Model):
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Объявление')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created_at']


# user_registrated = Signal(providing_args=["instance"])

