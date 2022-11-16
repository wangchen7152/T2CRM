# Generated by Django 3.2 on 2022-11-14 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0008_alter_linkman_sex'),
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerServe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serveType', models.IntegerField(db_column='serve_type', help_text='服务类型')),
                ('overview', models.CharField(db_column='overview', help_text='咨询描述', max_length=500)),
                ('state', models.IntegerField(db_column='state', help_text='服务状态')),
                ('serviceRequest', models.CharField(db_column='service_request', max_length=500)),
                ('assignTime', models.DateTimeField(db_column='assign_time', null=True)),
                ('serviceProce', models.CharField(db_column='service_proce', max_length=500, null=True)),
                ('serviceProcePeople', models.CharField(db_column='service_proce_people', max_length=50, null=True)),
                ('serviceProceTime', models.DateTimeField(db_column='service_proce_time', null=True)),
                ('serviceProceResult', models.CharField(db_column='service_proce_result', max_length=500, null=True)),
                ('myd', models.CharField(db_column='myd', max_length=50)),
                ('isValid', models.IntegerField(db_column='is_valid', default=1)),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
                ('deleted', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, help_text='是否删除')),
                ('assigner', models.ForeignKey(help_text='分配人', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ASUser', to='system.user')),
                ('createPeople', models.ForeignKey(help_text='创建人', on_delete=django.db.models.deletion.DO_NOTHING, related_name='CUser', to='system.user')),
                ('customer', models.ForeignKey(help_text='客户信息', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
            ],
            options={
                'verbose_name': '工作流表',
                'verbose_name_plural': '工作流表',
                'db_table': 't2_customer_serve',
            },
        ),
    ]