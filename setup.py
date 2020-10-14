from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as f:
        data = f.read()
        return data.split('\n')


def get_long_desc():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name = 'kiki',
    version = '1.0.1',
    description = 'pdf text-to-speech',
    long_description = get_long_desc(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/VijayStroup/Kiki',
    author = 'Vijay Stroup',
    author_email = 'vijay@vijaystroup.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires = get_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = """
        [console_scripts]
        kiki = kiki.kiki:main
    """
)
