import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dokr2',
     version='0.1',
     scripts=['dokr'] ,
     author="Deepak Kumar",
     author_email="safalsigdel@gmail.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )