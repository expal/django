# Generated by Django 3.2 on 2022-05-25 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Cost')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('availability_course', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('description_as_markdown', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('preview', models.CharField(max_length=255, verbose_name='Preview')),
                ('body', models.TextField(verbose_name='body')),
                ('body_as_markdown', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('num', models.PositiveIntegerField(verbose_name='Lesson number')),
                ('title', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='As markdown')),
                ('deleted', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.courses')),
            ],
            options={
                'ordering': ('course', 'num'),
            },
        ),
        migrations.CreateModel(
            name='CourseTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=128, verbose_name='Name')),
                ('name_second', models.CharField(max_length=128, verbose_name='Surname')),
                ('day_birth', models.DateField(verbose_name='Birth date')),
                ('deleted', models.BooleanField(default=False)),
                ('course', models.ManyToManyField(to='mainapp.Courses')),
            ],
        ),
    ]