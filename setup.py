import pathlib
from setuptools import setup,find_packages
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name="simple-p-file-downloader",

    version="1.0.0",
    description="Simple File downloader",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Manos Kounelakis",
    author_email="pkounelios@gmail.com",
    license="MIT",
    install_requires = [
        "requests"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["downloader"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pdownloader=downloader.__main__:main",
        ]
    },
)


