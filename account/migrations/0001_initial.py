# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import account.models
import django.utils.timezone
import account.validator
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=150, error_messages={'unique': 'A user with that username already exists.'}, validators=[account.validator.UnicodeUsernameValidator], help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, default=uuid.uuid4)),
                ('email', models.EmailField(max_length=254, unique=True, blank=True, verbose_name='email address', null=True)),
                ('is_participant', models.BooleanField(default=False)),
                ('is_researcher', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('experiments', models.ManyToManyField(to='experiment.Experiment')),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', blank=True, related_query_name='user', verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, default=uuid.uuid4)),
                ('age', models.IntegerField(blank=True, choices=[(8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120), (121, 121), (122, 122), (123, 123), (124, 124)], null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('education', models.CharField(max_length=100, blank=True, choices=[('did not complete highschool', 'Did not complete Highschool'), ('highschool/GED', 'Highschool/GED'), ('some college', 'Some College'), ("bachelor's degree", "Bachelor's Degree"), ("master's degree", "Master's Degree"), ('advanced or Ph.D', 'Advanced Graduate Work or Ph.D')], null=True)),
                ('gender', models.CharField(max_length=10, blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], null=True)),
                ('race', models.CharField(max_length=25, blank=True, choices=[('aboriginal indian', 'Aboriginal Indian'), ('asian', 'Asian'), ('black or african american', 'Black or African American'), ('white/caucasian', 'White/Caucasian'), ('hispanic or latino', 'Hispanic or Latino')], null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
