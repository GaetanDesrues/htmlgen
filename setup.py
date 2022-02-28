import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="htmlgen",
    version="0.1.000",
    author="Gaetan Desrues",
    author_email="gdesrues@gmail.com",
    url="https://github.com/GaetanDesrues/htmlgen",
    description="Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
