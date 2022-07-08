from setuptools import setup, find_packages

with open("requirements.txt","r") as f:
    reqs = f.readlines()

setup(
    name='tyxe',
    version='0.0.1',
    url='https://github.com/karalets/TyXe',
    author=['Hippolyt Ritter', 'Theofanis Karaletsos'],
    author_email='j.ritter@cs.ucl.ac.uk',
    description='BNNs for pytorch using pyro.',
    packages=find_packages(),
    install_requires=reqs,
)
