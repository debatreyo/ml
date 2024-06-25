# for auto-searching all installed packages in the project `src` folder
from setuptools import find_packages
from setuptools import setup
# for typing hints
from typing import List

# constants
HYPHEN_E_DOT = "-e ."

# helper function to parse `requirements.txt` file
def get_requirements(file_path: str) -> List[str]:
    """
    Opens and parses through the contents
    of `requirements.txt` file.

    Returns a list of all libraries
    mentioned inside `requirments.txt`.

    INPUT PARAMETERS ->
    `file_path`: (str) full file path
                of `requirements.txt`.
    """
    requirements = []

    with open(file_path) as file_object:
        # get a list with each line of file as a single element
        requirements = file_object.readlines() 
        # replace "\n" at end of each line of `requirements.txt`
        # which is present in each element of the list now
        requirements = [
            req.replace("\n", "")
            for req in requirements
        ]

        # check for presence of "-e ." in `requirements.txt` and discard
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
        
# setup project as a package for installation and distribution
setup(
    name="mlproject",
    version="0.0.1",
    author="Debatreyo",
    author_email="rayjonty18@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)