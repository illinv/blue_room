# Generated by Django 2.0.3 on 2018-04-24 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180402_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Middle'), ('H', 'High')], default='L', max_length=1, verbose_name='Приоритет фичи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bug',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
        ),
    ]