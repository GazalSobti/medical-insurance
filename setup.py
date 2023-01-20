from setuptools import find_packages, setup
from typing import List

requirement_file_name="requirements.txt"
REMOVE_PACKAGE="-e ."
def get_requirements()->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list=requirement_file.readline()
    requirement_list=[requirement_name.replace("\n","")for requirement_name in requirement_list]    
    
    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list    

# this function will return the list of  values from requirements.txt 


setup(name= "Insurance",
      version='0.0.1',
      description='Insurance industry project',
      author= 'Gazal Sobti',
      author_email='gazalsobti786@gmail.com',
      packages= find_packages(),
      install_reqires= get_requirements()
)
# find packages function will look for the folders having 
# __init__ file and store them to the packages variable
# i.e __init__ file is use to make the folder a package
# my email is req. to access my github repo. for extracting the data

# after complteting this file we install requirements.txt file and 
# Insurance.egg-info is formed