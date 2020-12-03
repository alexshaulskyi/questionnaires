# Generated by Django 3.1.3 on 2020-12-03 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=800)),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(default='quiz.png', upload_to='')),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPassedTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, max_length=4)),
                ('questions_answered_amount', models.IntegerField(blank=True, default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('questions_answered', models.ManyToManyField(blank=True, related_name='answered_questions', to='tests.Question')),
                ('selected_options', models.ManyToManyField(blank=True, related_name='selected_options', to='tests.Option')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_passed', to='tests.test')),
            ],
        ),
    ]
