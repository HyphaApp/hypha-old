# Generated by Django 2.0.13 on 2019-08-06 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application_projects', '0009_documentcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.TextField(choices=[('committed', 'Committed'), ('contracting', 'Contracting'), ('in_progress', 'In Progress'), ('closing', 'Closing'), ('complete', 'Complete')], default='committed'),
        ),
        migrations.AddField(
            model_name='approval',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application_projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='approval',
            unique_together={('project', 'by')},
        ),
    ]