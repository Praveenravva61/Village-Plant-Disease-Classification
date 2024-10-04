from setuptools import find_packages, setup
from typing import List

a = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Corrected this line
        requirements = [req.replace("\n", '') for req in requirements]
        
        if a in requirements:
            requirements.remove(a)
    return requirements

setup(
    name='Village Plant Diseases Classification',
    version='0.0.1',
    author='Ravva Praveen',
    author_email='praveen.ravva61@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
