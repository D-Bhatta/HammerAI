from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="hammerai",
    version="0.0.1",
    author="D-Bhatta",
    author_email="dbhatta1232@gmail.com",
    description="AI that can automate hammer usage in industrial robots",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/HammerAI",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License V3 (GPLv3",
    ],
)