from setuptools import setup

setup(
    name="masonite-api-pagination",
    version='0.0.1',
    packages=['masonite-api-pagination'],
    install_requires=[
        'masonite',
        'masonite-api'
    ],
    include_package_data=True,
)