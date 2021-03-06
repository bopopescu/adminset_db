# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('alarm_type', models.CharField(max_length=30)),
                ('send_mail', models.SmallIntegerField(default=0)),
                ('create_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'alarm',
            },
        ),
        migrations.CreateModel(
            name='AlarmTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('alarm_type', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'alarm_temp',
            },
        ),
        migrations.CreateModel(
            name='BackupLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_created=True, verbose_name='start datetime')),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
                ('type', models.CharField(choices=[('F', 'FULL'), ('I', 'INC'), ('B', 'BINLOG'), ('D', 'DUMP')], max_length=10, verbose_name='bakcup type:FULL,INC,BINLOG,DUMP')),
                ('end_date', models.DateTimeField(verbose_name='start datetime')),
                ('spend_time', models.IntegerField(verbose_name='spend time mi')),
                ('local_path', models.CharField(max_length=500, verbose_name='local path for backup saved')),
                ('remote_path', models.CharField(max_length=500, verbose_name='local path for backup saved')),
                ('is_copy_to_remote', models.IntegerField(null=True, verbose_name='flag scp backupfile to remote,0:NO,1:YES')),
                ('copy_date', models.DateTimeField(null=True, verbose_name='datetime to copy backupfile ')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='remote storage server ip ')),
            ],
        ),
        migrations.CreateModel(
            name='DBConfigInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='hostname')),
                ('ip', models.GenericIPAddressField(verbose_name='ip')),
                ('comment', models.CharField(max_length=200, verbose_name='comments')),
                ('backup_config', models.TextField(verbose_name='')),
                ('regdate', models.DateTimeField(verbose_name='\u589e\u66f4\u52a0\u6216\u8005\u6539\u65e5\u671f')),
            ],
        ),
        migrations.CreateModel(
            name='Mysql_processlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=20)),
                ('db_port', models.SmallIntegerField()),
                ('conn_id', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=32)),
                ('host', models.CharField(max_length=64)),
                ('db', models.CharField(max_length=64)),
                ('command', models.CharField(max_length=16)),
                ('time', models.IntegerField()),
                ('state', models.CharField(max_length=64, null=True)),
                ('info', models.TextField(null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'mysql_processlist',
            },
        ),
        migrations.CreateModel(
            name='Mysql_replication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=20)),
                ('db_port', models.SmallIntegerField()),
                ('is_master', models.SmallIntegerField(default=0)),
                ('is_slave', models.SmallIntegerField(default=0)),
                ('read_only', models.CharField(max_length=10, null=True)),
                ('gtid_mode', models.CharField(max_length=10, null=True)),
                ('master_server', models.CharField(max_length=30, null=True)),
                ('master_port', models.CharField(max_length=20, null=True)),
                ('slave_io_run', models.CharField(max_length=20, null=True)),
                ('slave_sql_run', models.CharField(max_length=20, null=True)),
                ('delay', models.CharField(max_length=20, null=True)),
                ('current_binlog_file', models.CharField(max_length=30, null=True)),
                ('current_binlog_pos', models.CharField(max_length=30, null=True)),
                ('master_binlog_file', models.CharField(max_length=30, null=True)),
                ('master_binlog_pos', models.CharField(max_length=30, null=True)),
                ('master_binlog_space', models.BigIntegerField(default=0)),
                ('slave_sql_running_state', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'mysql_replication',
            },
        ),
        migrations.CreateModel(
            name='Mysql_replication_his',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=20)),
                ('db_port', models.SmallIntegerField()),
                ('is_master', models.SmallIntegerField(default=0)),
                ('is_slave', models.SmallIntegerField(default=0)),
                ('read_only', models.CharField(max_length=10, null=True)),
                ('gtid_mode', models.CharField(max_length=10, null=True)),
                ('master_server', models.CharField(max_length=30, null=True)),
                ('master_port', models.CharField(max_length=20, null=True)),
                ('slave_io_run', models.CharField(max_length=20, null=True)),
                ('slave_sql_run', models.CharField(max_length=20, null=True)),
                ('delay', models.CharField(max_length=20, null=True)),
                ('current_binlog_file', models.CharField(max_length=30, null=True)),
                ('current_binlog_pos', models.CharField(max_length=30, null=True)),
                ('master_binlog_file', models.CharField(max_length=30, null=True)),
                ('master_binlog_pos', models.CharField(max_length=30, null=True)),
                ('master_binlog_space', models.BigIntegerField(default=0)),
                ('slave_sql_running_state', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'db_table': 'mysql_replication_his',
            },
        ),
        migrations.CreateModel(
            name='MysqlConnected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('connect_server', models.CharField(max_length=100)),
                ('connect_user', models.CharField(blank=True, max_length=50, null=True)),
                ('connect_db', models.CharField(blank=True, max_length=50, null=True)),
                ('connect_count', models.IntegerField()),
                ('create_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'db_table': 'mysql_connected',
            },
        ),
        migrations.CreateModel(
            name='MysqlStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('connect', models.SmallIntegerField(default=0)),
                ('role', models.CharField(default=-1, max_length=30)),
                ('uptime', models.IntegerField(default=-1)),
                ('version', models.CharField(max_length=50)),
                ('max_connections', models.SmallIntegerField(default=-1)),
                ('max_connect_errors', models.BigIntegerField(default=-1)),
                ('open_files_limit', models.IntegerField(default=-1)),
                ('open_files', models.SmallIntegerField(default=-1)),
                ('table_open_cache', models.SmallIntegerField(default=-1)),
                ('open_tables', models.SmallIntegerField(default=-1)),
                ('max_tmp_tables', models.SmallIntegerField(default=-1)),
                ('max_heap_table_size', models.IntegerField(default=-1)),
                ('max_allowed_packet', models.IntegerField(default=-1)),
                ('threads_connected', models.IntegerField(default=-1)),
                ('threads_running', models.IntegerField(default=-1)),
                ('threads_created', models.IntegerField(default=-1)),
                ('threads_cached', models.IntegerField(default=-1)),
                ('connections', models.IntegerField(default=-1)),
                ('aborted_clients', models.IntegerField(default=-1)),
                ('aborted_connects', models.IntegerField(default=-1)),
                ('connections_persecond', models.SmallIntegerField(default=-1)),
                ('bytes_received_persecond', models.IntegerField(default=-1)),
                ('bytes_sent_persecond', models.IntegerField(default=-1)),
                ('com_select_persecond', models.SmallIntegerField(default=-1)),
                ('com_insert_persecond', models.SmallIntegerField(default=-1)),
                ('com_update_persecond', models.SmallIntegerField(default=-1)),
                ('com_delete_persecond', models.SmallIntegerField(default=-1)),
                ('com_commit_persecond', models.SmallIntegerField(default=-1)),
                ('com_rollback_persecond', models.SmallIntegerField(default=-1)),
                ('questions_persecond', models.IntegerField(default=-1)),
                ('queries_persecond', models.IntegerField(default=-1)),
                ('transaction_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_disk_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_files_persecond', models.SmallIntegerField(default=-1)),
                ('table_locks_immediate_persecond', models.IntegerField(default=-1)),
                ('table_locks_waited_persecond', models.SmallIntegerField(default=-1)),
                ('key_buffer_size', models.BigIntegerField(default=-1)),
                ('sort_buffer_size', models.IntegerField(default=-1)),
                ('join_buffer_size', models.IntegerField(default=-1)),
                ('key_blocks_not_flushed', models.IntegerField(default=-1)),
                ('key_blocks_unused', models.IntegerField(default=-1)),
                ('key_blocks_used', models.IntegerField(default=-1)),
                ('key_read_requests_persecond', models.IntegerField(default=-1)),
                ('key_reads_persecond', models.IntegerField(default=-1)),
                ('key_write_requests_persecond', models.IntegerField(default=-1)),
                ('key_writes_persecond', models.IntegerField(default=-1)),
                ('innodb_version', models.CharField(default=b'-1', max_length=30)),
                ('innodb_buffer_pool_instances', models.SmallIntegerField(default=-1)),
                ('innodb_buffer_pool_size', models.BigIntegerField(default=-1)),
                ('innodb_doublewrite', models.CharField(default=b'-1', max_length=10)),
                ('innodb_file_per_table', models.CharField(default=b'-1', max_length=10)),
                ('innodb_flush_log_at_trx_commit', models.IntegerField(default=-1)),
                ('innodb_flush_method', models.CharField(default=b'-1', max_length=30)),
                ('innodb_force_recovery', models.IntegerField(default=-1)),
                ('innodb_io_capacity', models.IntegerField(default=-1)),
                ('innodb_read_io_threads', models.IntegerField(default=-1)),
                ('innodb_write_io_threads', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_total', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_data', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_dirty', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_flushed', models.BigIntegerField(default=-1)),
                ('innodb_buffer_pool_pages_free', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_misc', models.IntegerField(default=-1)),
                ('innodb_page_size', models.IntegerField(default=-1)),
                ('innodb_pages_created', models.BigIntegerField(default=-1)),
                ('innodb_pages_read', models.BigIntegerField(default=-1)),
                ('innodb_pages_written', models.BigIntegerField(default=-1)),
                ('innodb_row_lock_current_waits', models.CharField(max_length=100)),
                ('innodb_buffer_pool_pages_flushed_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_read_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_reads_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_write_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_read_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_inserted_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_updated_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_deleted_persecond', models.IntegerField(default=-1)),
                ('query_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('thread_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_read_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_write_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_blocks_used_rate', models.CharField(default=b'-1', max_length=10)),
                ('created_tmp_disk_tables_rate', models.CharField(default=b'-1', max_length=10)),
                ('connections_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_files_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_tables_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'mysql_status',
            },
        ),
        migrations.CreateModel(
            name='MysqlStatusHis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_ip', models.CharField(max_length=30)),
                ('db_port', models.CharField(max_length=10)),
                ('connect', models.SmallIntegerField(default=0)),
                ('role', models.CharField(default=-1, max_length=30)),
                ('uptime', models.IntegerField(default=-1)),
                ('version', models.CharField(max_length=50)),
                ('max_connections', models.SmallIntegerField(default=-1)),
                ('max_connect_errors', models.BigIntegerField(default=-1)),
                ('open_files_limit', models.IntegerField(default=-1)),
                ('open_files', models.SmallIntegerField(default=-1)),
                ('table_open_cache', models.SmallIntegerField(default=-1)),
                ('open_tables', models.SmallIntegerField(default=-1)),
                ('max_tmp_tables', models.SmallIntegerField(default=-1)),
                ('max_heap_table_size', models.IntegerField(default=-1)),
                ('max_allowed_packet', models.IntegerField(default=-1)),
                ('threads_connected', models.IntegerField(default=-1)),
                ('threads_running', models.IntegerField(default=-1)),
                ('threads_created', models.IntegerField(default=-1)),
                ('threads_cached', models.IntegerField(default=-1)),
                ('connections', models.IntegerField(default=-1)),
                ('aborted_clients', models.IntegerField(default=-1)),
                ('aborted_connects', models.IntegerField(default=-1)),
                ('connections_persecond', models.SmallIntegerField(default=-1)),
                ('bytes_received_persecond', models.IntegerField(default=-1)),
                ('bytes_sent_persecond', models.IntegerField(default=-1)),
                ('com_select_persecond', models.SmallIntegerField(default=-1)),
                ('com_insert_persecond', models.SmallIntegerField(default=-1)),
                ('com_update_persecond', models.SmallIntegerField(default=-1)),
                ('com_delete_persecond', models.SmallIntegerField(default=-1)),
                ('com_commit_persecond', models.SmallIntegerField(default=-1)),
                ('com_rollback_persecond', models.SmallIntegerField(default=-1)),
                ('questions_persecond', models.IntegerField(default=-1)),
                ('queries_persecond', models.IntegerField(default=-1)),
                ('transaction_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_disk_tables_persecond', models.SmallIntegerField(default=-1)),
                ('created_tmp_files_persecond', models.SmallIntegerField(default=-1)),
                ('table_locks_immediate_persecond', models.IntegerField(default=-1)),
                ('table_locks_waited_persecond', models.SmallIntegerField(default=-1)),
                ('key_buffer_size', models.BigIntegerField(default=-1)),
                ('sort_buffer_size', models.IntegerField(default=-1)),
                ('join_buffer_size', models.IntegerField(default=-1)),
                ('key_blocks_not_flushed', models.IntegerField(default=-1)),
                ('key_blocks_unused', models.IntegerField(default=-1)),
                ('key_blocks_used', models.IntegerField(default=-1)),
                ('key_read_requests_persecond', models.IntegerField(default=-1)),
                ('key_reads_persecond', models.IntegerField(default=-1)),
                ('key_write_requests_persecond', models.IntegerField(default=-1)),
                ('key_writes_persecond', models.IntegerField(default=-1)),
                ('innodb_version', models.CharField(default=b'-1', max_length=30)),
                ('innodb_buffer_pool_instances', models.SmallIntegerField(default=-1)),
                ('innodb_buffer_pool_size', models.BigIntegerField(default=-1)),
                ('innodb_doublewrite', models.CharField(default=b'-1', max_length=10)),
                ('innodb_file_per_table', models.CharField(default=b'-1', max_length=10)),
                ('innodb_flush_log_at_trx_commit', models.IntegerField(default=-1)),
                ('innodb_flush_method', models.CharField(default=b'-1', max_length=30)),
                ('innodb_force_recovery', models.IntegerField(default=-1)),
                ('innodb_io_capacity', models.IntegerField(default=-1)),
                ('innodb_read_io_threads', models.IntegerField(default=-1)),
                ('innodb_write_io_threads', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_total', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_data', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_dirty', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_flushed', models.BigIntegerField(default=-1)),
                ('innodb_buffer_pool_pages_free', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_pages_misc', models.IntegerField(default=-1)),
                ('innodb_page_size', models.IntegerField(default=-1)),
                ('innodb_pages_created', models.BigIntegerField(default=-1)),
                ('innodb_pages_read', models.BigIntegerField(default=-1)),
                ('innodb_pages_written', models.BigIntegerField(default=-1)),
                ('innodb_row_lock_current_waits', models.CharField(max_length=100)),
                ('innodb_buffer_pool_pages_flushed_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_read_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_reads_persecond', models.IntegerField(default=-1)),
                ('innodb_buffer_pool_write_requests_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_read_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_inserted_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_updated_persecond', models.IntegerField(default=-1)),
                ('innodb_rows_deleted_persecond', models.IntegerField(default=-1)),
                ('query_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('thread_cache_hitrate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_read_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_buffer_write_rate', models.CharField(default=b'-1', max_length=10)),
                ('key_blocks_used_rate', models.CharField(default=b'-1', max_length=10)),
                ('created_tmp_disk_tables_rate', models.CharField(default=b'-1', max_length=10)),
                ('connections_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_files_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('open_tables_usage_rate', models.CharField(default=b'-1', max_length=10)),
                ('create_time', models.DateTimeField(db_index=True)),
            ],
            options={
                'db_table': 'mysql_status_his',
            },
        ),
        migrations.CreateModel(
            name='RestoreLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_created=True, verbose_name='start datetime')),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
                ('type', models.CharField(max_length=100, verbose_name='Restore type:FULL,INC,BINLOG,DUMP')),
                ('restore_ip', models.GenericIPAddressField(verbose_name='resotre server ip')),
                ('restore_file', models.CharField(max_length=3000, verbose_name='restore files ')),
                ('restore_endpos', models.CharField(max_length=300, verbose_name='end of resotre datetime or binlog file pos')),
                ('end_date', models.DateTimeField(verbose_name='start datetime')),
                ('spend_time', models.IntegerField(verbose_name='spend time mi')),
                ('local_path', models.CharField(max_length=500, verbose_name='local path for backup saved')),
                ('remote_path', models.CharField(max_length=500, verbose_name='local path for backup saved')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='remote storage server ip ')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='mysqlstatushis',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
        migrations.AlterUniqueTogether(
            name='mysqlstatus',
            unique_together=set([('db_ip', 'db_port')]),
        ),
        migrations.AlterIndexTogether(
            name='mysqlconnected',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
        migrations.AlterIndexTogether(
            name='mysql_replication_his',
            index_together=set([('db_ip', 'db_port', 'create_time')]),
        ),
        migrations.AlterUniqueTogether(
            name='mysql_replication',
            unique_together=set([('db_ip', 'db_port')]),
        ),
        migrations.AlterIndexTogether(
            name='alarmtemp',
            index_together=set([('db_ip', 'db_port', 'alarm_type')]),
        ),
        migrations.AlterIndexTogether(
            name='alarm',
            index_together=set([('db_ip', 'db_port')]),
        ),
    ]
