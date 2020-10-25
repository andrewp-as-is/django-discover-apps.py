__all__ = ['discover_apps']


import os
import setuptools

"""
import django_discover_apps

INSTALLED_APPS = django_discover_apps.discover_apps(".") + [
    ...
]
"""

APPS_FILES = [
    'admin.py',
    'apps.py',
    'models.py',
]
APPS_DIRS = [
    'admin',
    'apps',
    'models',
    'templatetags'
]


def isapp(path):
    if os.path.exists(os.path.join(path, 'management', 'commands')):
        return os.path.join(path)
    if not os.path.exists(os.path.join(path, '__init__.py')):
        return False
    for app_file in APPS_FILES:
        fullpath = os.path.join(path, app_file)
        if os.path.exists(fullpath) and os.path.isfile(fullpath):
            return True
    for app_dir in APPS_DIRS:
        fullpath = os.path.join(path, app_dir, '__init__.py')
        if os.path.exists(fullpath) and os.path.isfile(fullpath):
            return True


def discover_apps(path):
    """return a list of apps"""
    apps = []
    for package in setuptools.find_packages(os.path.abspath(path)):
        if 'views' not in package.split('.') and 'urls' not in package.split('.'):
            if isapp(os.path.join(path, package.replace('.', os.sep))):
                apps.append(package)
    return apps
