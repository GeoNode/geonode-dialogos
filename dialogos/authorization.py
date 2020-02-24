from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from django.utils.importlib import import_module
except ImportError:
    from importlib import import_module


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = import_module(module)
    except ImportError as error:
        raise ImproperlyConfigured(
            "Error importing {0}: '{1}'".format(module, error))
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured(
            "Module {0} does not define a {1}".format(module, attr))
    return attr


def default_can_delete(user, comment):
    if user.is_superuser:
        return True
    return user == comment.author


def default_can_edit(user, comment):
    return user == comment.author


def load_can_delete():
    import_path = getattr(settings, "COMMENTS_CAN_DELETE_CALLABLE", None)

    if import_path is None:
        return default_can_delete

    return load_path_attr(import_path)


def load_can_edit():
    import_path = getattr(settings, "COMMENTS_CAN_EDIT_CALLABLE", None)

    if import_path is None:
        return default_can_edit

    return load_path_attr(import_path)
