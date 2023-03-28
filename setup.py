import setuptools
import os

def get_version():
    """
    Return the version string based on the current Git tag, or a default
    value of "0.0.1" if the tag cannot be determined.
    """
    if "GITHUB_REF" in os.environ:
        tag_ref = os.environ["GITHUB_REF"]
        if tag_ref.startswith("refs/tags/"):
            return tag_ref[len("refs/tags/"):]
    return "0.0.1"

def get_readme_long():
    with open("README.md", "r") as f:
        return f.read()

setuptools.setup(
    name="selenium-print",
    packages=setuptools.find_packages(),
    version=get_version(),
    license="MIT",
    description="A minimal printing utility based on selenium and chrome that is able to render any HTML to PDF.",
    author="Henry Müssemann",
    author_email="henry@muessemann.de",
    url="https://github.com/bubblegumsoldier/selenium-print",
    long_description=get_readme_long(),
    long_description_content_type="text/markdown",
    keywords=["print", "pdf", "converter", "selenium"],
    install_requires=['selenium'],
)
