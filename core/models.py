from django.db import models


class ProjectManager:
    pass


class Project(models.Model):
    """
    Сущность проекта. Хранит в себе всю информацию о проекте:
    Описание, бизнес-логику, пароли, репозитории, бэклог
    """
    title = models.CharField(verbose_name='Название проекта', max_length=200)
    description = models.TextField(verbose_name='Описание проекта')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(verbose_name='Имя фичи', max_length=200)
    description = models.TextField(verbose_name='Описание фичи')
    project = models.ForeignKey('Project', verbose_name='Проект', related_name='project', on_delete=models.CASCADE)
    is_release = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Bug(models.Model):
    title = models.CharField(verbose_name='Имя бага', max_length=200)
    description = models.TextField(verbose_name='Описание бага')
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class TestCase(models.Model):
    """
    Тестовый случай для фичи.
    Требуется для описания ситуаций, которые могут привести к неккоректному функционированию приложения"""
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    case = models.TextField(verbose_name='Тестовый случай')
    expected_behavior = models.TextField(verbose_name='Ожидаемое поведение')


