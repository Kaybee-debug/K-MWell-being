# Generated by Django 4.2.3 on 2023-07-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Height', models.FloatField()),
                ('Weight', models.FloatField()),
                ('Age', models.FloatField()),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=250)),
                ('Level', models.CharField(choices=[('Biginner', 'Biginner'), ('moderate', 'moderate'), ('professional', ' professional')], default='Biginner', max_length=250)),
            ],
        ),
    ]
