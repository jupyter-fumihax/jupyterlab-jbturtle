from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()
long_license = (this_directory / 'LICENSE').read_text()

setup(
    name = 'jbturtle',
    version = '0.2.7',
    install_requires = [ 'Pillow' ],
    description = 'Simple turtle system for JupyterLab',
    author='Fumi.Iseki',
    author_email='fumi.hax@gmail.com',
    packages = find_packages(),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = long_license,
    url = 'https://github.com/fiseki/jupyterlab-jbturtle',
    download_url = 'https://github.com/fiseki/jupyterlab-jbturtle',
)

