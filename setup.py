from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'VerificationEmail for Python'


# Setting up

setup(
    name="VerificationEmailC",
    version=VERSION,
    author="SamuraiCoder",
    author_email="<aelboutaheri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['GeneratorFEC'],
    keywords=['python', 'email', 'random', 'smtplib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
