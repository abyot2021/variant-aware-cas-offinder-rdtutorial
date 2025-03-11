import io
import setuptools


with io.open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssam",
    version="1.1.2",
    author="Jeongbin Park",
    author_email="jeongbin.park@pusan.ac.kr",
    description="SSAM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pnucolab/ssam",
    packages=setuptools.find_packages(),
)
