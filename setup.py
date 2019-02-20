"""
    Purpose:
        setup.py is executed to build the python package
"""

# Python Imports
from os import listdir
from setuptools import setup, find_packages
import re


###
# Helper Functions
###


def get_version_from_file(python_version_file="./VERSION"):
    """
    Purpose:
        Get python requirements from a specified requirements file.
    Args:
        python_requirements_file (String): Path to the requirements file (usually
            it is requirements.txt in the same directory as the setup.py)
    Return:
        requirements (List of Strings): The python requirements necessary to run
            the library
    """

    version = "unknown"
    with open(python_version_file) as version_file:
        version = version_file.readline().strip().strip("\n")

    return version


def get_requirements_from_file(python_requirements_file="./requirements.txt"):
    """
    Purpose:
        Get python requirements from a specified requirements file.
    Args:
        python_requirements_file (String): Path to the requirements file (usually
            it is requirements.txt in the same directory as the setup.py)
    Return:
        requirements (List of Strings): The python requirements necessary to run
            the library
    """

    requirements = []
    with open(python_requirements_file) as requirements_file:
        requirement = requirements_file.readline()
        while requirement:
            if requirement.strip().startswith("#"):
                pass
            elif requirement.strip() == "":
                pass
            else:
                requirements.append(requirement.strip())
            requirement = requirements_file.readline()

    return requirements


def get_requirements_from_packages(packages):
    """
    Purpose:
        Get python requirements for each package. will get requirements file
        in each package's subdirectory
    Args:
        packages (String): Name of the packages
    Return:
        requirements (List of Strings): The python requirements necessary to run
            the library
    """

    requirements = []
    for package in packages:
        package_dir = package.replace(".", "/")
        requirement_files = get_requirements_files_in_package_dir(package_dir)

        for requirement_file in requirement_files:
            package_requirements =\
                get_requirements_from_file(python_requirements_file=requirement_file)
            requirements = requirements + package_requirements

    return list(set(requirements))


def get_requirements_files_in_package_dir(package_dir):
    """
    Purpose:
        From a package dir, find all requirements files (Assuming form requirements.txt
        or requirements_x.txt)
    Args:
        package_dir (String): Directory of the package
    Return:
        requirement_files (List of Strings): Requirement Files
    """

    requirements_regex = r"^requirements[_\w]*.txt$"

    requirement_files = []
    for requirement_file in listdir(f"./{package_dir}"):
        if re.match(requirements_regex, requirement_file):
            requirement_files.append(f"./{package_dir}/{requirement_file}")

    return requirement_files


###
# Main Functionality
###


def main():
    """
    Purpose:
        Main function for packaging and setting up packages
    Args:
        N/A
    Return:
        N/A
    """

    # Get Version
    version = get_version_from_file()

    # Get Packages
    packages = find_packages()
    install_packages = [package for package in packages if not package.endswith(".tests")]
    test_packages = [package for package in packages if package.endswith(".tests")]

    # Get Requirements and Requirments Installation Details
    install_requirements = get_requirements_from_packages(install_packages)
    test_requirements = get_requirements_from_packages(test_packages)
    setup_requirements = ["pytest-runner", "pytest", "pytest-cov"]

    # Get Dependency Links For Each Requirement (As Necessary)
    dependency_links = []

    setup(
        name="ctodd-python-lib-avro",
        version=version,
        python_requires=">3.0,<3.7",
        description=("Python utilities used for interacting with .avro/.avsc files"),
        url="https://github.com/ChristopherHaydenTodd/ctodd-python-lib-avro",
        author="Christopher H. Todd",
        author_email="Christopher.Hayden.Todd@gmail.com",
        classifiers=["Programming Language :: Python"],
        keywords=["python", "libraries", "avro", "avsc"],
        packages=packages,
        install_requires=install_requirements,
        setup_requires=setup_requirements,
        tests_require=test_requirements,
        project_urls={},
    )


if __name__ == "__main__":
    main()
