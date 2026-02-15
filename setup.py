from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    hypen = '-e .'
    with open(file_path) as f:
      requirements = f.readlines()
      requirements = [req.replace("\n", "") for req in requirements]
      if hypen in requirements: requirements.remove(hypen)

    return requirements


setup(
    name="ml_projects_1",
    version="0.1",
    packages=find_packages(),
    author="Anupriya Baskar",
    install_requires=get_requirements('req.txt'),
)