command = '/opt/venv/bin/gunicorn'
pythonpath = '/opt/venv/emrapp'
bind = '127.0.0.1:8001'
workers = 4
user = 'nobody'
env = 'DJANGO_SETTINGS_MODULE=emrapp.settings'

