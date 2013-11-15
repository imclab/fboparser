from django.core.management.base import CommandError, BaseCommand
from django.conf import settings
import os
from fboparser.fbo_raw.importer import import_file

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        PATHNAME =  settings.PROJECT_ROOT + '/raw_files/'
        print(PATHNAME)

        for f in os.listdir(PATHNAME):
            if os.path.isfile(PATHNAME + f):
                print('Processing file: %s' % f)
                total_notices = import_file(PATHNAME + f, encoding='iso8859_2')
                print("total notices: %s" % total_notices)