from setuptools  import find_packages
from setuptools  import setup

f=open("README.md","r")
readme_file=f.read()
f.close()


setup(

        name         = "pyframe3dd",
        version      = "0.0.2",
        description  = "estructural analysis using frame3dd",
        author       = "Edwin Pareja",
        author_email = "edwinsaulpm@gmail.com",
        url          = "https://www.illarisoft.com/",
        long_description=readme_file,
        long_description_content_type="text/markdown",
        packages=find_packages(),

        )
