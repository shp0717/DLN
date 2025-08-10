import setuptools, DLN.meta as meta

setuptools.setup(
    name=meta.__package__,
    version=meta.__version__,
    packages=setuptools.find_packages(),
    install_requires=meta.__used_pypi_packages__,
    author=meta.__author__,
    author_email=meta.__email__,
    description=meta.__doc__,
    long_description=meta.__readme__,
    long_description_content_type="text/markdown",
    url=meta.__git__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=meta.__python_version__,
)
