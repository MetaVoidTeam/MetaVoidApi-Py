import setuptools

with open("README.md", "r") as k:
    long_description = k.read()

setuptools.setup(
    name="MetaVoid-Py",
    version="0.8",
    author="MetaVoidTeam",
    description="Simple MetaVoid API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MetaVoidTeam/MetaVoid-Py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=["requests"]
)
