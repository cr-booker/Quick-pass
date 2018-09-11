import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick-pass",
    version="1.0.0",
    author="Christopher Booker",
    author_email="cryanb91@gmail.com",
    description="A password/passphrase generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syst3m-failur3/Quick-pass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3),
        "Operating System :: OS Independent",
    ],
    entry_points={
          'console_scripts': ['quick-pass=quickpass:main']
    },
    include_package_data=True
    )
