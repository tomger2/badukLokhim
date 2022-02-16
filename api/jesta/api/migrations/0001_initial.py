# Generated by Django 3.2.12 on 2022-02-16 16:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=120)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('apartment_num', models.IntegerField(blank=True, null=True)),
                ('private_home', models.BooleanField()),
                ('phone', models.CharField(max_length=12)),
                ('long', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('title', models.CharField(max_length=60)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Son',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('elder', models.ManyToManyField(to='api.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('active_cities', models.JSONField()),
                ('phone', models.CharField(max_length=12)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('num_of_calls', models.IntegerField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profession', models.ManyToManyField(to='api.Profession')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(verbose_name=False)),
                ('is_occupied', models.BooleanField(verbose_name=False)),
                ('description', models.CharField(max_length=1024)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('closed_date', models.DateField(blank=True, null=True)),
                ('destination', models.JSONField()),
                ('elder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.elder')),
                ('grandson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.son')),
                ('handy_man', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chosen', to='api.pro')),
                ('handy_man_pool', models.ManyToManyField(to='api.Pro')),
                ('profession', models.ManyToManyField(to='api.Profession')),
            ],
        ),
    ]
