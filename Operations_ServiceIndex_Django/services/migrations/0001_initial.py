# Generated by Django 4.1.1 on 2022-09-16 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.IntegerField()),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'db_table': '"serviceindex"."availability"',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': '"serviceindex"."event"',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=256)),
                ('ip_address', models.CharField(blank=True, max_length=128)),
                ('qualys', models.BooleanField()),
                ('nagios', models.BooleanField()),
                ('label', models.CharField(max_length=128)),
                ('note', models.CharField(blank=True, max_length=2048)),
                ('host_last_verified', models.DateField(blank=True, null=True)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.availability')),
            ],
            options={
                'db_table': '"serviceindex"."host"',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('hostname', models.CharField(blank=True, max_length=256)),
                ('failover_process', models.CharField(blank=True, max_length=1024)),
                ('failover_last_tested', models.DateField(blank=True, null=True)),
                ('service_last_verified', models.DateField(blank=True, null=True)),
                ('dependencies', models.CharField(blank=True, max_length=1024)),
                ('lb', models.BooleanField()),
                ('ha', models.BooleanField()),
                ('otp', models.BooleanField()),
                ('nagios', models.BooleanField()),
                ('deprecated', models.BooleanField(default=False)),
            ],
            options={
                'db_table': '"serviceindex"."service"',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=256)),
            ],
            options={
                'db_table': '"serviceindex"."site"',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': '"serviceindex"."staff"',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.CharField(max_length=256)),
            ],
            options={
                'db_table': '"serviceindex"."support"',
            },
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=16)),
                ('msg', models.CharField(max_length=1024)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'db_table': '"serviceindex"."logentry"',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'db_table': '"serviceindex"."link"',
            },
        ),
        migrations.CreateModel(
            name='HostEventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('unchecked', 'unchecked'), ('in_progress', 'in progress'), ('compliant', 'compliant'), ('na', 'N/A')], max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.event')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.host')),
            ],
            options={
                'db_table': '"serviceindex"."hosteventstatus"',
            },
        ),
        migrations.CreateModel(
            name='HostEventLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=16)),
                ('note', models.CharField(blank=True, max_length=2048)),
                ('status', models.CharField(choices=[('unchecked', 'unchecked'), ('in_progress', 'in progress'), ('compliant', 'compliant'), ('na', 'N/A')], max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.event')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.host')),
            ],
            options={
                'db_table': '"serviceindex"."hosteventlog"',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.site'),
        ),
        migrations.AddField(
            model_name='host',
            name='poc_backup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poc_backup_instance_set', to='services.staff'),
        ),
        migrations.AddField(
            model_name='host',
            name='poc_primary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poc_primary_instance_set', to='services.staff'),
        ),
        migrations.AddField(
            model_name='host',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='host',
            name='support',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.support'),
        ),
        migrations.AddField(
            model_name='host',
            name='sys_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sys_admin_instance_set', to='services.staff'),
        ),
        migrations.CreateModel(
            name='EditLock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=16)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'db_table': '"serviceindex"."editlock"',
            },
        ),
    ]
