import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "br-nome-gen",
    version = "1.3.0",
    author = "Victor Williams Stafusa da Silva",
    author_email = "victorwssilva@gmail.com",
    description = "A generator of Brazilian typical names.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/victorwss/br-nome-gen",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)