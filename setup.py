from setuptools import setup

setup(
    name = 'gopro2gpx',
    author = 'Juan M. Casillas + TobsA',
    url = 'https://github.com/TobsA13/gopro2gpx.git',
    version = "0.2",
    packages = ['gopro2gpx'],
    entry_points = {
        'console_scripts': ['gopro2gpx = gopro2gpx.gopro2gpx:main']
    }
)
