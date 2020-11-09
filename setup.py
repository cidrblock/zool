from setuptools import setup

setup(
    name="zool",
    version="0.1.0",
    author="cidrblock",
    packages=["zool"],
    entry_points={
        "console_scripts": [
            "zool = zool.zool:main",
        ],
    },
    install_requires=["jinja2", "pyyaml", "requests", "pygments", "lxml"],
)
