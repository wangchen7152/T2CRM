# Generated by Django 3.2 on 2022-10-29 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='城市名称')),
                ('add_time', models.DateField(verbose_name=datetime.datetime.now)),
                ('des', models.CharField(max_length=200, verbose_name='u描述')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
                'db_table': 'T2_user_city',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('salt', models.CharField(max_length=4, verbose_name='盐加密')),
                ('truename', models.CharField(max_length=20, null=True, verbose_name='昵称')),
                ('email', models.CharField(max_length=30, null=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='电话号码')),
                ('state', models.IntegerField(default=0, verbose_name='状态')),
                ('isValid', models.IntegerField(db_column='is_valid', default=1, verbose_name='是否可用')),
                ('createDate', models.DateTimeField(db_column='create_date', default=datetime.datetime.now, verbose_name='创建时间')),
                ('updateDate', models.DateTimeField(db_column='update_date', null=True, verbose_name='更新时间')),
                ('company', models.CharField(max_length=24, null=True, verbose_name='所属公司')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'T2_user',
            },
        ),
    ]
