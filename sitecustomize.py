import pandas as pd

_original_init = pd.DataFrame.__init__

def _patched_init(self, data=None, index=None, *args, **kwargs):
    if isinstance(index, set):
        index = list(index)
    return _original_init(self, data, index, *args, **kwargs)

pd.DataFrame.__init__ = _patched_init
