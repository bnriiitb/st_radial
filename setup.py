import setuptools
from pathlib import Path

README = (Path(__file__).parent/"README.md").read_text()

setuptools.setup(
    name="st_radial",
    version="1.0.0",
    author="akshanshkmr",
    author_email="akshanshkmr821@gmail.com",
    description="A streamlit component to display metrics neatly",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/akshanshkmr/st_radial",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.87",
    ],
)