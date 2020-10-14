from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as f:
        data = f.read()
        return data.split('\n')


setup(
    name = 'kiki',
    version = '1.0',
    description = 'pdf text-to-speech',
    author = 'Vijay Stroup',
    url = 'https://github.com/VijayStroup/Kiki',
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
