# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0015_english_british_teds_twos'),
    ]

    operations = [
        migrations.CreateModel(
            name='English_British_TEDS_Threes',
            fields=[
                ('basetable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable')),
                ('item_1', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_2', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_3', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_4', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_5', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_6', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_7', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_8', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_9', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_10', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_11', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_12', models.CharField(max_length=7, null=True, choices=[('simple', 'simple'), ('complex', 'complex')])),
                ('item_13', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_14', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_15', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_16', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_17', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_18', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_19', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_20', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_21', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_22', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_23', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_24', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_25', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_26', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_27', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_28', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_29', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_30', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_31', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_32', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_33', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_34', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_35', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_36', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_37', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_38', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_39', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_40', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_41', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_42', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_43', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_44', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_45', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_46', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_47', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_48', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_49', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_50', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_51', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_52', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_53', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_54', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_55', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_56', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_57', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_58', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_59', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_60', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_61', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_62', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_63', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_64', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_65', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_66', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_67', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_68', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_69', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_70', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_71', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_72', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_73', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_74', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_75', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_76', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_77', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_78', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_79', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_80', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_81', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_82', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_83', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_84', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_85', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_86', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_87', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_88', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_89', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_90', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_91', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_92', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_93', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_94', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_95', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_96', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_97', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_98', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_99', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_100', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_101', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_102', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_103', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_104', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_105', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_106', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_107', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_108', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_109', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_110', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_111', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_112', models.CharField(max_length=8, null=True, choices=[('produces', 'produces')])),
                ('item_113', models.CharField(max_length=9, null=True, choices=[('often', 'often'), ('sometimes', 'sometimes'), ('not yet', 'not yet')])),
            ],
            bases=('instruments.basetable',),
        ),
    ]