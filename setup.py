import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hdfviewer", # Replace with your own username
    version="0.0.1",
    author="James Jhang",
    author_email="e8315402@gmail.com",
    description="Show HDF file content.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl-gitlab.csie.ntut.edu.tw/e8315402/hdf-viewer.git",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)