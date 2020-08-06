from django.db import models


DEFAULT_STATUS = 'new'
DEFAULT_TYPE = 'task'

STATUS_CHOICES = [
    (DEFAULT_STATUS, 'Новый'),
    ('in_progress', 'В процессе'),
    ('done', 'Выполнено'),
]

TYPE_CHOICES = [
    (DEFAULT_TYPE, 'Задача'),
    ('bug', 'Ошибка'),
    ('enhancement', 'Улучшение')
]


class Status(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, choices=STATUS_CHOICES,
                            default=DEFAULT_STATUS, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, choices=TYPE_CHOICES,
                            default=DEFAULT_TYPE, verbose_name='Тип задачи')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.PROTECT, verbose_name='Задача')
    type = models.ForeignKey('webapp.Type', related_name='types', on_delete=models.PROTECT, verbose_name='Type')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.pk} {self.summary}'
