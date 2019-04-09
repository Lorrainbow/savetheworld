import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="savetheworld",
    version="0.0.1",
    author="Phil Underwood",
    author_email="beardydoc@gmail.com",
    description="Useful code for the 'Save the World with code' book",
    long_description=long_description,
    url="https://github.com/furbrain/savetheworld",
    packages=setuptools.find_packages(),
    install_requires=["touchphat"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
