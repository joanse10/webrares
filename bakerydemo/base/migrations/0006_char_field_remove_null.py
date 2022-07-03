# Generated by Django 3.2.10 on 2021-12-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_formfield_clean_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_1_title',
            field=models.CharField(blank=True, default='', help_text='Title to display above the promo copy', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_2_title',
            field=models.CharField(blank=True, default='', help_text='Title to display above the promo copy', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_section_3_title',
            field=models.CharField(blank=True, default='', help_text='Title to display above the promo copy', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='promo_title',
            field=models.CharField(blank=True, default='', help_text='Title to display above the promo copy', max_length=255),
            preserve_default=False,
        ),
    ]
