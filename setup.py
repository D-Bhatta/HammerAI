from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="hammerai",
    version="0.0.5",
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

""" Build:
pip install -r requirements_dev.txt
pip install -e .
git checkout -b <branch-name>
# Make changes
pytest
pytest --cov=hammerai
# If tests pass, delete all build artefacts
python setup.py sdist bdist_wheel
git commit -a -m "message"
git push origin <branch-name>
# Create pull request on github
# Merge PR
twine upload -r testpypi dist/*"""