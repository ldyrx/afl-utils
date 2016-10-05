import os
import uuid
from django.db import models


class Index(models.Model):
    job = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sync_dir = models.CharField(max_length=500, unique=True, default=os.getcwd)


class Fuzzers(models.Model):
    job = models.ForeignKey('Index', on_delete=models.PROTECT)
    fuzzer = models.CharField(max_length=200)
    fuzzer_pid = models.IntegerField(null=True)
    command_line = models.CharField(max_length=1000)
    afl_banner = models.CharField(max_length=200)  # target_000
    afl_version = models.CharField(max_length=10)  # 2.35b


class Stats(models.Model):
    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(
            self.last_update, self.start_time, self.cycles_done, self.execs_done, self.execs_per_sec, self.paths_total,
            self.paths_favored, self.paths_found, self.paths_imported, self.max_depth, self.cur_path,
            self.pending_favs, self.pending_total, self.variable_paths, self.stability, self.bitmap_cvg,
            self.unique_crashes, self.unique_hangs, self.last_path, self.last_crash, self.last_hang,
            self.execs_since_crash, self.exec_timeout)

    fuzzer = models.ForeignKey('Fuzzers', on_delete=models.PROTECT)
    start_time = models.IntegerField() # 1475080845
    last_update = models.IntegerField() # 1475081950
    cycles_done = models.IntegerField() # 0
    execs_done = models.IntegerField() # 372033733
    execs_per_sec = models.FloatField() # 1546.82
    paths_total = models.IntegerField() # 420
    paths_favored = models.IntegerField() # 25
    paths_found = models.IntegerField() # 0
    paths_imported = models.IntegerField() # 83
    max_depth = models.IntegerField() # 39
    cur_path = models.IntegerField() # 650
    pending_favs = models.IntegerField() # 0
    pending_total = models.IntegerField() # 0
    variable_paths = models.IntegerField() # 0
    stability = models.FloatField() # 100.00 %
    bitmap_cvg = models.FloatField() # 18.37 %
    unique_crashes = models.IntegerField() # 0
    unique_hangs = models.IntegerField() # 13
    last_path = models.IntegerField() # 1475081940
    last_crash = models.IntegerField() # 0
    last_hang = models.IntegerField() # 0
    execs_since_crash = models.IntegerField() # 63393
    exec_timeout = models.IntegerField() # 800


class Results(models.Model):
    fuzzer = models.ForeignKey('Fuzzers', on_delete=models.PROTECT)
    sample = models.CharField(max_length=500)
    classification = models.CharField(max_length=100)
    classification_description = models.CharField(max_length=200)
    hash = models.CharField(max_length=65)
    comment = models.CharField(max_length=1000)
