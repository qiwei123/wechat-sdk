try:
    import simplejson
except ImportError:
    try:
        import json as simplejson
    except ImportError:
        raise ImportError("A json library is required to use this python library")
