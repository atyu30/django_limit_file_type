from django.db import models
from validatedfile.fields import ValidatedFileField
import time

class TestModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    the_file = ValidatedFileField(
                    null = True,
                    blank = True,
                    upload_to = 'files/%Y/%m/%d',
                    content_types = ['image/png','image/jpeg','application/mp4','application/pdf','application/zip','application/gzip'],
                    max_upload_size = 1024000)

