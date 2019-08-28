# Generated by Django 2.2.2 on 2019-08-04 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('image_post', models.ImageField(upload_to='post_images')),
                ('files', models.FileField(upload_to='myFiles')),
                ('caption', models.TextField()),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_comment', models.CharField(max_length=100)),
                ('comm', models.TextField()),
                ('date_commented', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.POST')),
            ],
        ),
    ]
