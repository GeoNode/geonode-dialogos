# #!/usr/bin/env python
# import os
# import sys

# from django.conf import settings
# from django.test.simple import DjangoTestSuiteRunner


# if not settings.configured:
#     settings.configure(
#         DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3"}},
#         ROOT_URLCONF="dialogos.urls",
#         INSTALLED_APPS=[
#             "django.contrib.auth",
#             "django.contrib.contenttypes",
#             "django.contrib.sessions",
#             "dialogos",
#         ]
#     )


# def runtests(*test_args):
#     if not test_args:
#         test_args = ["dialogos"]
#     parent = os.path.dirname(os.path.abspath(__file__))
#     sys.path.insert(0, parent)
#     suite = DjangoTestSuiteRunner(verbosity=1, interactive=True)
#     failures = suite.run_tests(test_args)
#     sys.exit(failures)


# if __name__ == "__main__":
#     runtests(*sys.argv[1:])

#!/usr/bin/env python

import os
import sys
import tempfile

import django
from django.conf import settings
from django.test.utils import get_runner

ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.join(ROOT, '..')
sys.path.append(APP_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


MEDIA_ROOT = os.path.join(tempfile.gettempdir(), 'dialogos')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(os.path.join(MEDIA_ROOT, 'test'))
settings.MEDIA_ROOT = MEDIA_ROOT


if __name__ == "__main__":
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['dialogos'], verbosity=1)
    if failures:
        sys.exit(failures)
