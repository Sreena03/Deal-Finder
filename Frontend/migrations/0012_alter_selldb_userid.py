# Generated by Django 4.1.7 on 2024-05-29 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0011_alter_selldb_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='UserId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Frontend.registerdb'),
            preserve_default=False,
        ),
    ]