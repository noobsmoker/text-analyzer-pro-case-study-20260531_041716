from setuptools import setup, find_packages

setup(
    name="text-analyzer-pro-case-study-20260531_041716",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'text=text:main',
        ],
    },
)
