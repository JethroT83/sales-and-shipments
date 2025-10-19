from django.apps import AppConfig
from django.conf import settings
from support.helpers import env
from support.debug import var_dump, dd
# @see https://github.com/MrBin99/django-vite/issues/161
class HttpLibConfig(AppConfig):
    name = "app.http.lib"

    var_dump("HttpLibConfig.ready() running…")

    def ready(self):
        if settings.ENV.lower() == 'production':
            return

        from django_vite.core.asset_loader import DjangoViteAppClient
        from urllib.parse import urljoin

        def get_dev_server_url(self, path: str) -> str:

            base = f"{self.dev_server_protocol}://{self.dev_server_host}:{self.dev_server_port}/"

            var_dump(base, urljoin(base, path.lstrip("/")))
            return urljoin(base, path.lstrip("/"))

        DjangoViteAppClient.get_dev_server_url = get_dev_server_url