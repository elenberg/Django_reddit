#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    env = os.environ.get("LK_ENV", None)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % env)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
