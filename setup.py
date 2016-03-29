from setuptools import setup

setup(
    name='runningstats',
    version='0.1.0',
    description='A numpy aware running statistics module',
    url='http://github.com/MaxNoe/runningstats',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=['runningstats'],
    install_requires=[
        'numpy',
    ],
)
