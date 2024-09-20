import re
import socket

from django.core.management.base import CommandError
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management.commands.runserver import naiveip_re
from django.conf import settings

from constance import config

class Command(RunserverCommand):
    default_addr = "0.0.0.0"

    def add_arguments(self, parser):
        parser.add_argument(
            "--addrport", 
            default="8000", 
            required=False,
            help="Optional port number, or ipaddr:port"
        )
        parser.add_argument(
            "--ipv6",
            "-6",
            action="store_true",
            dest="use_ipv6",
            help="Tells Django to use an IPv6 address.",
        )
        parser.add_argument(
            "--nothreading",
            action="store_false",
            dest="use_threading",
            help="Tells Django to NOT use threading.",
        )
        parser.add_argument(
            "--noreload",
            action="store_false",
            dest="use_reloader",
            help="Tells Django to NOT use the auto-reloader.",
        )
        parser.add_argument(
            "--skip-checks",
            action="store_true",
            help="Skip system checks.",
        )
        parser.add_argument("message",
            type=str,
            default="Hello World!",
            nargs='+',
            help="Message to return response from index.",
        )

    def handle(self, *args, **options):
        if not settings.DEBUG and not settings.ALLOWED_HOSTS:
            raise CommandError("You must set settings.ALLOWED_HOSTS if DEBUG is False.")
        
        # Do custom message
        config.MESSAGE = ' '.join(options["message"])
        print("Setting up the return response to {}". format(config.MESSAGE))

        self.use_ipv6 = options["use_ipv6"]
        if self.use_ipv6 and not socket.has_ipv6:
            raise CommandError("Your Python does not support IPv6.")
        self._raw_ipv6 = False
        if not options["addrport"]:
            self.addr = ""
            self.port = self.default_port
        else:
            m = re.match(naiveip_re, options["addrport"])
            if m is None:
                raise CommandError(
                    '"%s" is not a valid port number '
                    "or address:port pair." % options["addrport"]
                )
            self.addr, _ipv4, _ipv6, _fqdn, self.port = m.groups()
            if not self.port.isdigit():
                raise CommandError("%r is not a valid port number." % self.port)
            if self.addr:
                if _ipv6:
                    self.addr = self.addr[1:-1]
                    self.use_ipv6 = True
                    self._raw_ipv6 = True
                elif self.use_ipv6 and not _fqdn:
                    raise CommandError('"%s" is not a valid IPv6 address.' % self.addr)
        if not self.addr:
            self.addr = self.default_addr_ipv6 if self.use_ipv6 else self.default_addr
            self._raw_ipv6 = self.use_ipv6
        self.run(**options)
