from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup (
    name = 'sarcastifier',
    version = '0.0.1',
    author = 'teddy',
    author_email = 'udefined@right.now',
    license = 'The Unlicense',
    description = 'Make normal text sarcastic',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/tedaco1/sarcastifier',
    py_modules = ['sarcastifier', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.10',
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cooltool=sarcastify:cli
   '''
)