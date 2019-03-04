from setuptools import setup, find_packages
from i3altlayout.i3altlayout import VERSION

setup(name='i3altlayout',
      description='alternating layouts for i3',
      version=VERSION,
      packages=find_packages(),
      author='deadc0de6',
      author_email='deadc0de6@foo.bar',
      license='GPLv3',
      keywords='i3 wm',
      entry_points={
            'console_scripts': [
                  'i3altlayout=i3altlayout.i3altlayout:main',
                  ],
            },
      )


