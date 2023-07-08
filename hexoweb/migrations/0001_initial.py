# Generated by Django 3.2.18 on 2023-07-07 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2147483647)),
                ('content', models.TextField(blank=True, max_length=2147483647)),
            ],
        ),
        migrations.CreateModel(
            name='CustomModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2147483647)),
                ('content', models.TextField(blank=True, max_length=2147483647)),
            ],
        ),
        migrations.CreateModel(
            name='FriendModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2147483647)),
                ('url', models.TextField(max_length=2147483647)),
                ('imageUrl', models.TextField(max_length=2147483647)),
                ('time', models.TextField(max_length=2147483647)),
                ('description', models.TextField(max_length=2147483647)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2147483647)),
                ('url', models.TextField(max_length=2147483647)),
                ('size', models.TextField(max_length=2147483647)),
                ('date', models.TextField(max_length=2147483647)),
                ('type', models.TextField(max_length=2147483647)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.TextField(max_length=2147483647)),
                ('label', models.TextField(blank=True, max_length=2147483647)),
                ('content', models.TextField(blank=True, max_length=2147483647)),
            ],
        ),
        migrations.CreateModel(
            name='SettingModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2147483647)),
                ('content', models.TextField(blank=True, max_length=2147483647)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticPV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticUV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='TalkModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, max_length=2147483647)),
                ('tags', models.TextField(blank=True, max_length=2147483647)),
                ('time', models.TextField(max_length=2147483647)),
                ('like', models.TextField(blank=True, default='[]', max_length=2147483647)),
                ('values', models.TextField(default='{}', max_length=2147483647)),
            ],
        ),
    ]