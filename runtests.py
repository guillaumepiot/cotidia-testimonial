#!/usr/bin/env python
import sys

import django

from django.conf import settings

sys.path.append('../')

DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        "django_otp",
        "django_otp.plugins.otp_static",
        "django_otp.plugins.otp_totp",
        "two_factor",

        "cotidia.core",
        "cotidia.admin",
        "cotidia.mail",
        "cotidia.account",
        "cotidia.testimonial",
        "rest_framework",
        "rest_framework.authtoken",
    ],
    MIDDLEWARE_CLASSES=[
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django_otp.middleware.OTPMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "cotidia.account.middleware.AccountMiddleware",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            "OPTIONS": {
                "debug": True,
                "context_processors": [
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                ]
            }
        },
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    SITE_URL="http://localhost:8000",
    APP_URL="http://localhost:8000",
    ROOT_URLCONF="cotidia.testimonial.tests.urls",
    SECRET_KEY="notasecret",
    AUTH_USER_MODEL="account.User",
    AUTHENTICATION_BACKENDS=[
        'cotidia.account.auth.EmailBackend',
    ],
    STATIC_URL='/static/'
)


def runtests(*test_args):

    # parent = os.path.dirname(os.path.abspath(__file__))
    # parent += "/cotidia"
    # print("path", parent)
    # sys.path.insert(0, parent)

    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    # Compatibility with Django 1.7's stricter initialization
    if hasattr(django, "setup"):
        django.setup()

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ["cotidia.testimonial.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ["tests"]

    failures = runner_class(
        verbosity=1,
        interactive=True,
        failfast=False
    ).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
