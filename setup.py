from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Javahar_Bongu',
    author_email='javahar999@gmail.com',
    packages=find_packages(), #searches for the "__init__.py" files in the entire project and make them as a packages
    install_requires=get_requirements('requirements.txt')
)

'''NOTE : -e . triggers the setup.py file while installing packages therefore setup.py file also runs to build the packages'''