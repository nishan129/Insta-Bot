from setuptools import setup, find_packages
from typing import List , Any


def get_requirements() -> List[str]:
    requirements_list : List[str] = []
    
    return requirements_list

setup(
    name= "Insta-Bot",
    version= "0.0.0.0",
    author= "Nishant Borkar",
    author_email= "nishantborkar139@gmail.com",
    description="InstaGram Chat Bot",
    packages=find_packages(),
    install_requires=get_requirements()
)