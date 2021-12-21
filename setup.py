from setuptools import find_packages, setup

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='edtime',
    version='1.0.1',
    description="Extended Decimal Time",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/mindey/edtime',
    author='Mindey',
    author_email='~@mindey.com',
    license='MIT',
    packages = find_packages(exclude=['docs', 'tests*', 'media*']),
    install_requires=[
    ],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False,
    entry_points = {
        'console_scripts': [
        ],
    }
)
