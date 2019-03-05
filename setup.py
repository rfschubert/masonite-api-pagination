from setuptools import setup

setup(
    name="masonite-api-pagination",
    author="Raphael Schubert",
    author_email="rfswdp@gmail.com",
    description="Simple yet powerful masonite-api pagination",
    url="https://github.com/rfschubert/masonite-api-pagination",
    version='0.0.3',
    packages=['masonite-api-pagination'],
    install_requires=[
        'masonite',
        'masonite-api'
    ],
    include_package_data=True,
)