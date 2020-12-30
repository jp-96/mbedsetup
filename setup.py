from setuptools import setup, find_packages

setup(
    name="mbedsetup",
	version="0.1",
    author='jp.rad',
    author_email='jp.rad@outlook.jp',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'patch',
        'jsonschema',
        'pyelftools',
    ]
)