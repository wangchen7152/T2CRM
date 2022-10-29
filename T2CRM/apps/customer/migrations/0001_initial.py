# Generated by Django 3.2 on 2022-10-29 19:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=64, verbose_name='城市名称')),
            ],
            options={
                'verbose_name': '客户信息表',
                'verbose_name_plural': '客户信息表',
                'db_table': 't2_city_customer',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('khno', models.CharField(max_length=20, unique=True, verbose_name='客户编号')),
                ('name', models.CharField(max_length=20, verbose_name='客户名称')),
                ('area', models.CharField(max_length=20, verbose_name='所在地区')),
                ('cusManager', models.CharField(db_column='cus_manager', max_length=30)),
                ('level', models.CharField(max_length=30, verbose_name='客户级别')),
                ('myd', models.CharField(max_length=30, verbose_name='客户满意度')),
                ('xyd', models.CharField(max_length=30, verbose_name='信用度')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('postCode', models.CharField(db_column='post_code', max_length=10)),
                ('phone', models.CharField(max_length=18)),
                ('fax', models.CharField(max_length=20)),
                ('web_url', models.CharField(db_column='web_url', max_length=50)),
                ('company_num', models.CharField(max_length=50, verbose_name='营业注册号')),
                ('leader_of_company', models.CharField(max_length=20, verbose_name='法人')),
                ('registered_capital', models.CharField(max_length=64, verbose_name='注册资本')),
                ('annual_turnover', models.CharField(max_length=20, verbose_name='年营业额')),
                ('bank', models.CharField(max_length=20, verbose_name='开户银行')),
                ('bank_number', models.CharField(max_length=20, verbose_name='开户账号')),
                ('land_tax', models.CharField(max_length=20, verbose_name='地税')),
                ('the_irs', models.CharField(max_length=20, verbose_name='国税')),
                ('state', models.IntegerField(default=0)),
                ('isValid', models.IntegerField(db_column='is_valid', default=1)),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
                ('city', models.ForeignKey(db_column='city_id', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.city', verbose_name='所属城市')),
            ],
            options={
                'verbose_name': '客户信息表',
                'verbose_name_plural': '客户信息表',
                'db_table': 't2_customer',
            },
            managers=[
                ('all', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLoss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusNo', models.CharField(db_column='cus_no', max_length=40)),
                ('cusName', models.CharField(db_column='cus_name', max_length=20)),
                ('cusManager', models.CharField(db_column='cus_manager', max_length=20)),
                ('lastOrderTime', models.DateTimeField(db_column='last_order_time')),
                ('confirmLossTime', models.DateTimeField(db_column='confirm_loss_time')),
                ('state', models.IntegerField()),
                ('lossReason', models.CharField(db_column='loss_reason', max_length=1000)),
                ('isValid', models.IntegerField(db_column='is_valid', default=1)),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
            ],
            options={
                'verbose_name': '客户流失情况表',
                'verbose_name_plural': '客户流失情况表',
                'db_table': 't2_customer_loss',
            },
        ),
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.DateTimeField(db_column='order_no')),
                ('orderDate', models.DateTimeField(auto_now_add=True, db_column='order_date')),
                ('address', models.CharField(db_column='address', max_length=120)),
                ('totalPrice', models.FloatField(db_column='total_price')),
                ('state', models.IntegerField(choices=[(0, '未回款'), (1, '已回款')], verbose_name='是否回款')),
                ('isValid', models.IntegerField(db_column='is_valid')),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
                ('customer', models.ForeignKey(db_column='cus_id', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
            ],
            options={
                'verbose_name': '客户订单',
                'verbose_name_plural': '客户订单',
                'db_table': 't2_customer_order',
            },
        ),
        migrations.CreateModel(
            name='LinkMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusId', models.IntegerField(db_column='cus_id')),
                ('linkName', models.CharField(db_column='link_name', max_length=20)),
                ('sex', models.CharField(max_length=4)),
                ('zhiwei', models.CharField(db_column='zhiwei', max_length=20)),
                ('officePhone', models.CharField(db_column='office_phone', max_length=20)),
                ('phone', models.CharField(db_column='phone', max_length=20)),
                ('isValid', models.IntegerField(db_column='is_valid', default=1)),
                ('createDate', models.DateTimeField(db_column='create_date', default=datetime.datetime.now)),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
            ],
            options={
                'verbose_name': '客户联系人表',
                'verbose_name_plural': '客户联系人表',
                'db_table': 't2_customer_linkman',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=64, verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '客户信息表',
                'verbose_name_plural': '客户信息表',
                'db_table': 't2_province',
            },
        ),
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsName', models.CharField(db_column='goods_name', max_length=100)),
                ('goodsNum', models.IntegerField(db_column='goods_num')),
                ('unit', models.CharField(db_column='unit', max_length=10)),
                ('price', models.FloatField(db_column='price')),
                ('sum', models.FloatField(db_column='sum')),
                ('isValid', models.IntegerField(db_column='is_valid')),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customerorders')),
            ],
            options={
                'verbose_name': '客户订单详情表',
                'verbose_name_plural': '客户订单详情表',
                'db_table': 't2_order_details',
            },
        ),
        migrations.CreateModel(
            name='CustomerReprieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(db_column='measure', max_length=1000)),
                ('isValid', models.IntegerField(db_column='is_valid', default=1)),
                ('createDate', models.DateTimeField(auto_now_add=True, db_column='create_date')),
                ('updateDate', models.DateTimeField(auto_now_add=True, db_column='update_date')),
                ('customerLoss', models.ForeignKey(db_column='loss_id', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customerloss')),
            ],
            options={
                'verbose_name': '客户六十暂缓措施表',
                'verbose_name_plural': '客户六十暂缓措施表',
                'db_table': 't2_customer_reprieve',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='city_province',
            field=models.ForeignKey(db_column='city_province_id', on_delete=django.db.models.deletion.DO_NOTHING, to='customer.province'),
        ),
    ]
