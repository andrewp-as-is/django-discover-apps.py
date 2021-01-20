import setuptools

setuptools.setup(
    name='django-discover-apps',
    version='2021.1.20',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
