# Generated by Django 2.0 on 2018-04-09 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0045_auto_20171122_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='next_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wizard_builder.Page'),
        ),
    ]
