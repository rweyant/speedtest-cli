from setuptools import setup,find_packages
setup(
    name = 'speedrecorder',
    version = '0.1',
    packages = find_packages(),
    install_requires=[
    'ipgetter',
    'requests']
)
