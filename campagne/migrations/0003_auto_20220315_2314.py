# Generated by Django 3.2.6 on 2022-03-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0002_auto_20220315_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team_ptr',
        ),
        migrations.AddField(
            model_name='player',
            name='color',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
