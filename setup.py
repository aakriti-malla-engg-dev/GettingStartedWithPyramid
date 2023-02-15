from setuptools import setup, find_packages

setup(
    name='GettingStartedWithPyramid',
    version='0.1',
    packages=find_packages(),
    url='',
    license='',
    author='aakritimalla',
    author_email='',
    description='',
    install_requires=[
        'pyramid',
        'pymongo',
        'waitress',

    ],
    include_package_data=True,
    entry_points={
        'paste.app_factory': [
            'main = GettingStartedWithPyramid:main'
        ],
    },
)
