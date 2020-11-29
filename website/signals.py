from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from django.urls import resolve
from . models import Visit
from django.db.utils import OperationalError, IntegrityError


@receiver(request_started)
def signal_request_started(sender, **kwargs):
    environ = kwargs.get("environ")
    ip_address = environ.get("REMOTE_ADDR")
    url = environ.get("PATH_INFO")
    url_name = resolve(url).url_name
    app_name = resolve(url).app_name

    if app_name != "admin" and url_name:
        try:
            Visit.objects.create(ip_address=ip_address, app_name=app_name,
                                 url=url, url_name=url_name)
        except Exception as err:
            print(err)


@ receiver(request_finished)
def signal_request_finished(sender, **kwargs):
    print("Request finished!")
