from setuptools import setup, find_packages

setup(
    name='python-hello_world',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'hello_world=hello_world.main:main',
        ],
    },
)