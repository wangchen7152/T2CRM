# Generated by Django 3.2 on 2022-11-14 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('serve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerserve',
            name='assigner',
            field=models.ForeignKey(help_text='分配人', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ASUser', to='system.user'),
        ),
        migrations.AlterField(
            model_name='customerserve',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, db_column='create_date', null=True),
        ),
        migrations.AlterField(
            model_name='customerserve',
            name='myd',
            field=models.CharField(db_column='myd', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customerserve',
            name='updateDate',
            field=models.DateTimeField(auto_now_add=True, db_column='update_date', null=True),
        ),
    ]