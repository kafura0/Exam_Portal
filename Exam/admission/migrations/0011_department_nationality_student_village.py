# Generated by Django 3.2.24 on 2024-04-08 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0010_auto_20240330_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(default='select', max_length=150)),
                ('first_Name', models.CharField(default='select', max_length=150)),
                ('other_Name', models.CharField(default='select', max_length=150)),
                ('email', models.EmailField(default='example@example.com', max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('reg_No', models.CharField(default='23u764', max_length=20, unique=True)),
                ('phone', models.CharField(default='234', max_length=25, unique=True)),
                ('fee_status', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(blank=True, default='avatar', upload_to='profile_pic/Student/')),
                ('home_Address', models.CharField(max_length=40)),
                ('mother_Maiden_name', models.CharField(max_length=200)),
                ('matrix_No', models.CharField(default='2003/csc-0001', max_length=20)),
                ('admission_status', models.BooleanField(default=False)),
                ('start_class', models.DateField(auto_now_add=True)),
                ('semester', models.IntegerField(default=1)),
                ('academic_session', models.CharField(default='2022/2023', max_length=20)),
                ('programme_duration', models.IntegerField(default=4)),
                ('graduation_year', models.IntegerField(default=2026)),
                ('admitted_Department', models.ForeignKey(default='Computer Science', on_delete=django.db.models.deletion.CASCADE, to='admission.department')),
                ('admitted_programme', models.ForeignKey(default='Not Admitted', on_delete=django.db.models.deletion.CASCADE, to='admission.programme')),
                ('local_Government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.lga')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.nationality')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.state')),
                ('village_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.village')),
            ],
            options={
                'verbose_name_plural': 'Students Personal Information',
            },
        ),
    ]
