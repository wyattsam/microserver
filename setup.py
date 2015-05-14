from setuptools import setup

requires = [
    "Flask==0.10.1",
    "PyYAML==3.11",
    "pymongo==3.0.1"
]

setup(
    name="microserver",
    version="0.0.1",
    packages=["microserver"],
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=requires,
    tests_require=requires,
)
