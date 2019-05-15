import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="savetheworld",
    version="0.0.4",
    author="Lorraine Underwood",
    author_email="lorrainbow@gmail.com",
    description="Useful code for the 'Save the World with code' book",
    long_description=long_description,
    url="https://github.com/Lorrainbow/savetheworld",
    packages=setuptools.find_packages(),
    install_requires=["touchphat"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
