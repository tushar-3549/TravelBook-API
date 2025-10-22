#!/usr/bin/env python
import os
import sys

def main():
    # .env থেকে DEBUG ভ্যালু পড়বে
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    
    # DEBUG=True হলে local.py, না হলে prod.py লোড করবে
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "nol_backend.settings.local" if debug_mode else "nol_backend.settings.prod"
    )

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
