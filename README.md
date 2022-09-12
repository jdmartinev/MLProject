# MLProject

1. Set virtual environment with Pipenv

Pipenv is a Python package and dependency manager for Python projects. It harnessess the power of different existing tools, bringing their functionalities togheter:

- **pip** for Python package management
- **pienv** for Python version management
- **virtualenv** for creating different virtual Python environments
- **pipfile** for managing project dependencies

1. To install pipenv, we need Python and pip. In the command line, please check Python and pip versions:

python -V
pip -V

2. If both Python and pip are already installed, type the following line:

pip install pipenv

3. Once pipenv has been installed, create a new project directory for new virtual environment, and navigate into it.

mkdir MLProj && cd MLProj

4. Create a new virtual environment and generate Pipfile:

pipenv install

5. Activate the virtual environment 

pipenv shell

6. Your command prompt should now be similar to (MLProj) juanmartinez@DESKTOP-UNIN5CI:/mnt/c/Users/juanm/OneDrive - Universidad EAFIT/Cursos/Proyecto integrador/MLProject$

7. To install any package inside your virtual environment, type

pipenv install <package>

pipenv install keras

