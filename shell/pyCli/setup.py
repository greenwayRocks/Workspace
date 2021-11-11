from setuptools import setup, find_packages

setup(
    name="jformat",
    description="json file formatting cli-tool",
    author="Satish Adhikari",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["click"],
    entry_points="""
    [console_scripts]
    jformat=cli:main
    """
)
