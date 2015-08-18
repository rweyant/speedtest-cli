from setuptools import setup,find_packages
setup(
    name = 'Internet Speed Recorder',
    version = '0.1',
    packages = find_packages(),
    install_requires=[
    'ipgetter',
    'requests']
)