#!/usr/bin/python
from django.core.management.base import BaseCommand, CommandError
from catalogue.models import Book
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Scans a folder to update the books database'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('path', nargs=1, type=str)

        # Named (optional) arguments
        # See the argparse Python documentation for more about add_argument usage
        #parser.add_argument(
        #    '--delete',
        #    action='store_true',
        #    dest='delete',
        #    help='Delete poll instead of closing it',
        #)

    def handle(self, *args, **options):
         COUNT = 10
         DIR = options['path'][0]
         for root, dirs, files in os.walk(DIR):
             COUNT -= 1
             if not COUNT:
                 break
             #path = root.split(os.sep)
             basename = os.path.basename(root)
             for file in files:
                  args = {'filepath':root, 'filename':file, 'title':file, 'description':'', 'category':None, 'tags':basename, 'seen':timezone.now()}
                  #self.stdout.write("record is %s" % str(args))
                  #Book.objects.create(**args)
                  Book.objects.update_or_create(
                       filename=file,
                       defaults=args,
                  )
         self.stdout.write(self.style.SUCCESS('Successfully scanned folder %s.' % DIR))


