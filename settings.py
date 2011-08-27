# global settings (versioned)
from os import path

DEBUG = False

APPROOT = path.dirname(path.abspath(__file__))

# YOUTUBE_API_KEY = ''

# sensitive and deploy-specific settings (untracked)
local_settings_path = path.join(APPROOT, 'local_settings.py')
if path.exists(local_settings_path):
    # use execfile to allow modifications within this context
    execfile(local_settings_path)
