from setuptools import setup, find_packages

setup(
    name='chgnet',
    version='1.0',
    packages=find_packages(include=["chgnet", "chgnet.*"]),
    install_requires=[
        "numpy",
        "torch==1.12.0",
        "ase",
        "pymatgen",
        "tqdm",
    ],
)