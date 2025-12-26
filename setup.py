"""setup.py"""
from os import path
from setuptools import setup, find_packages
from i3altlayout.i3altlayout import VERSION


README = 'README.md'
here = path.abspath(path.dirname(__file__))
REQUIRES_PYTHON = '>=3.4'
URL = f'https://github.com/deadc0de6/i3altlayout/archive/v{VERSION}.tar.gz'


def read_readme(readme_path):
    """read readme content"""
    with open(readme_path, encoding="utf-8") as file:
        return file.read()


setup(
    name='i3altlayout',
    version=VERSION,

    description='i3wm efficient real estate',
    long_description=read_readme(README),
    long_description_content_type='text/markdown',
    license_files=('LICENSE',),
    url='https://github.com/deadc0de6/i3altlayout',
    download_url=URL,
    options={"bdist_wheel": {"python_tag": "py3"}},
    # include anything from MANIFEST.in
    include_package_data=True,

    author='deadc0de6',
    author_email='deadc0de6@foo.bar',

    license='GPLv3',
    python_requires=REQUIRES_PYTHON,
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            'Programming Language :: Python :: 3.14',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          ],

    keywords='i3wm tiling',
    packages=find_packages(exclude=['tests*']),
    install_requires=['docopt', 'i3ipc'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['pycodestyle', 'pyflakes'],
    },

    entry_points={
          'console_scripts': [
                'i3altlayout=i3altlayout.i3altlayout:cli',
                ],
          },
)
