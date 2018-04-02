from django.db import models


class ProjectManager(models.Manager):
    def get_features_by_project_id(self, pk):
        return Feature.objects.filter(project=pk)

    def get_bugs_by_project_id(self, pk):
        return Bug.objects.filter(feature__project=pk)

    def get_planed_time_project(self, pk):
        pass


class Project(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=200)
    description = models.TextField(verbose_name='Описание проекта')
    created_time = models.DateTimeField(verbose_name='Дата начала', auto_created=True)

    objects = ProjectManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(verbose_name='Имя фичи', max_length=200)
    description = models.TextField(verbose_name='Описание фичи')
    project = models.ForeignKey('Project', verbose_name='Проект', related_name='project', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_created=True)
    planned_time = models.FloatField(verbose_name='Планируемое время в часах')

    is_release = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Bug(models.Model):
    title = models.CharField(verbose_name='Имя бага', max_length=200)
    description = models.TextField(verbose_name='Описание бага')
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_created=True)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class TestCase(models.Model):
    feature = models.ForeignKey('Feature', verbose_name='Связная фича', on_delete=models.CASCADE)
    case = models.TextField(verbose_name='Тестовый случай')
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_created=True)
    expected_behavior = models.TextField(verbose_name='Ожидаемое поведение')

    def __str__(self):
        return self.case

    def __unicode__(self):
        return self.case


class Issue(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_time = models.DateTimeField(verbose_name='Дата создания', auto_created=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
