import os
from django.core.wsgi import get_wsgi_application

# Debug flag দেখে settings সিলেক্ট করা
debug_mode = os.getenv("DEBUG", "False").lower() == "true"

if debug_mode:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nol_backend.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nol_backend.settings.prod")

application = get_wsgi_application()

# Auto migrate if enabled
if os.environ.get("DJANGO_AUTO_MIGRATE") == "1":
    try:
        from django.core.management import call_command
        call_command("migrate", interactive=False)
        print("[AUTO-MIGRATE] OK")
    except Exception as e:
        print(f"[AUTO-MIGRATE] Error: {e}")
