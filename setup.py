from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as f:
        data = f.read()
        return data.split('\n')


setup(
    name = 'kiki',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    install_requires = get_requirements(),
    entry_points = """
        [console_scripts]
        kiki=kiki.kiki:main
    """
)
