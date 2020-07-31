# Generated by Django 2.2.13 on 2020-07-01 10:19

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('determinations', '0010_add_determination_stream_field_forms'),
        ('funds', '0076_multi_input_char_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoundBaseDeterminationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='determinations.DeterminationForm')),
                ('round', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='determination_forms', to='funds.RoundBase')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabBaseDeterminationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='determinations.DeterminationForm')),
                ('lab', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='determination_forms', to='funds.LabBase')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationBaseDeterminationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('application', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='determination_forms', to='funds.ApplicationBase')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='determinations.DeterminationForm')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]