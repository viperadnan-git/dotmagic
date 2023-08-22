from setuptools import find_packages, setup

from dotmagic import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dotmagic",
    version=version,
    author="Adnan Ahmad",
    author_email="viperadnan@gmail.com",
    description="A Python library for accessing environment variables using dot notation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    url="https://github.com/viperadnan-git/dotmagic",
    download_url=f"https://github.com/viperadnan-git/gdnan/archive/v{version}.tar.gz",
    keywords=["environment", "variables", "dotenv", "env", "config", "configuration"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements,
)
