Where are the Django source files?

If you have difficulty finding where the Django source files are located on your system, run the following command:

$ python -c "
import sys
sys.path = sys.path[1:]
import django
print(django.__path__)"