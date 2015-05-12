from setuptools import setup

requires = [
    "Flask==0.10.1",
    "Jinja2==2.7.3",
    "MarkupSafe==0.23",
    "Werkzeug==0.10.4",
    "itsdangerous==0.24",
    "wsgiref==0.1.2",
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
