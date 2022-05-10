from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="security-package",
    version="0.0.1",
    author="Sarah Soares Gonçalves da Silva",
    author_email="contatodev.sarah@gmail.com",
    description="Pacote feito para Aplicações de Segurança utilizando Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)