from .production import *

try:
    from .local import *
except:
    pass

try:
    from .my_settings import *
except:
    pass