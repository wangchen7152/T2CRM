# Generated by Django 3.2 on 2022-11-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20221104_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerloss',
            name='confirmLossTime',
            field=models.DateTimeField(db_column='confirm_loss_time', null=True),
        ),
        migrations.AlterField(
            model_name='customerloss',
            name='deleted',
            field=models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, null=True, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='customerloss',
            name='isValid',
            field=models.IntegerField(db_column='is_valid', default=1, null=True),
        ),
        migrations.AlterField(
            model_name='customerloss',
            name='lastOrderTime',
            field=models.DateTimeField(db_column='last_order_time', null=True),
        ),
        migrations.AlterField(
            model_name='customerloss',
            name='lossReason',
            field=models.CharField(db_column='loss_reason', max_length=1000, null=True),
        ),
    ]