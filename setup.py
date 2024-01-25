from setuptools import setup

from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pramda",
    version="1.2.0",
    description="Functional programming for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Myuksal",
    author_email="jupyter@kakao.com",
    packages=[f for f in setuptools.find_packages() if not f.endswith("_test.py")],
    zip_safe=False,
    python_requires=">=3.10",
    license="MIT",
    url="http://github.com/pramda/pramda",
    keywords=["function", "tool", "ramda"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
