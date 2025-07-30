from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('fonts/ds_digital', ['fonts/ds_digital/DS-DIGIT.TTF'])
]
OPTIONS = {
    'argv_emulation': False,
    'packages': ['PyQt5'],
    'resources': ['fonts/ds_digital/DS-DIGIT.TTF'],
    'includes': ['logging'],
    'iconfile': None
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
