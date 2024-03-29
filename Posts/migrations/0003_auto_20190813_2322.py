# Generated by Django 2.2.2 on 2019-08-13 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20190812_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Title_comment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Posts.POST'),
        ),
    ]
