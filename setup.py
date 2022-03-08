import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textscrub",
    version="1.0.0",
    author=["Pragya Verma", "Reeya Pimple"],
    author_email=["vpragya@uw.edu", "reeyapb@uw.edu"],
    description="Instance in an Instant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reeya26/TextScrubPkg",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)