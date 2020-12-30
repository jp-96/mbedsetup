from setuptools import setup, find_packages

setup(
    name="mbedsetup",
	version="0.1.1",
    author='jp.rad',
    author_email='jp.rad@outlook.jp',
    license='MIT',
    packages=find_packages(),
    package_data={'': ['*.patch']},
    entry_points={
        'console_scripts': [
            'mbedsetup=mbedsetup:main',
        ],
    },
    install_requires=[
        'patch',
        'jsonschema',
        'pyelftools',
    ]
)