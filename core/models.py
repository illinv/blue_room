from itertools import chain
from django.db import models
from django.utils.functional import cached_property


class ProjectManager(models.Manager):
    def get_features_by_project_id(self, pk):
        return Feature.objects.filter(project=pk)

    def get_bugs_by_project_id(self, pk):
        return Bug.objects.filter(feature__project=pk)

    def get_issues_by_project_id(self, pk):
        return Issue.objects.filter(project=pk)

    def get_count_features(self, pk):
        return Feature.objects.filter(project=pk).count()

    def get_in_work_features_and_bugs(self, pk):
        features = Feature.objects.filter(project=pk, status=Feature.IN_WORK_STATUS)
        bugs = Bug.objects.filter(feature__project=pk)
        return list(chain(features, bugs))

    def get_planed_time_project(self, pk):
        pass


class Project(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=200)
    description = models.TextField(verbose_name='Описание проекта')
    created_time = models.DateTimeField(verbose_name='Дата начала', auto_now_add=True)

    objects = ProjectManager()

    @cached_property
    def count_features(self):
        return Feature.objects.filter(project=self.pk).count()

    @cached_property
    def count_bugs(self):
        return Bug.objects.filter(feature__project=self.pk).count()

    @cached_property
    def count_open_issues(self):
        return Issue.objects.filter(project=self.pk).count()

    @cached_property
    def features(self):
        return Feature.objects.filter(project=self)

    @cached_property
    def bugs(self):
        return Bug.objects.filter(feature__project=self)

    @cached_property
    def issues(self):
        return Issue.objects.filter(project=self)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Feature(models.Model):
    LOW_PRIORITY = 'L'
    MIDDLE_PRIORITY = 'M'
    HIGH_PRIORITY = 'H'

    PRIORITY = (
        (LOW_PRIORITY, 'Low'),
        (MIDDLE_PRIORITY, 'Middle'),
        (HIGH_PRIORITY, 'High'),
    )

    NEW_STATUS = 'N'
    IN_WORK_STATUS = 'IW'
    REVIEW_STATUS = 'RW'
    CANCELED_STATUS = 'C'
    COMPLETED_STATUS = 'E'

    STATUSES = (
        (NEW_STATUS, 'New'),
        (IN_WORK_STATUS, 'In work'),
        (REVIEW_STATUS, 'Ready for a review'),
        (CANCELED_STATUS, 'Canceled'),
        (COMPLETED_STATUS, 'Completed')
    )

    title = models.CharField(verbose_name='Имя фичи', max_length=200)
    description = models.TextField(verbose_name='Описание фичи')
    project = models.ForeignKey('Project', verbose_name='Проект', related_name='project', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    planned_time = models.FloatField(verbose_name='Планируемое время в часах')

    is_release = models.BooleanField(default=False)
    priority = models.CharField(verbose_name='Приоритет фичи', max_length=1, choices=PRIORITY)
    status = models.CharField(verbose_name='Статус', max_length=2, choices=STATUSES)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Bug(models.Model):
    title = models.CharField(verbose_name='Имя бага', max_length=200)
    description = models.TextField(verbose_name='Описание бага')
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class TestCase(models.Model):
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    case = models.TextField(verbose_name='Тестовый случай')
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    expected_behavior = models.TextField(verbose_name='Ожидаемое поведение')

    def __str__(self):
        return self.case

    def __unicode__(self):
        return self.case


class Issue(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Article(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
