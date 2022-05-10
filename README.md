
# Security_Package

## Description

The package security_package is used to:
- **arq_testes**: files TXT for testing the modules of the package.
- **ping_kit**: tests with ping and multiples pings.
- **udp_kit**: tests client-server using socket.
- **tool_kit**: multiples tools for security.
	- **generators**: password gernerator and permutation of words.
	- **hash_kit**: generator and comparator of hashes.
	- **ip_tool**:  	
		-  Convert IP Address.
		-  Discover Network Address.
		- Get Informations (IP, Hostname, City, Region) of an IP Address.
	- **web_kit**:  
		- GUI tool for open specifics browsers.
		- Web Scrapping.
		- Web Crawling.
	- **ocult_arq.py**: ocult files in a specific directory/path.
	- **phone_tool.py**: country name and region detection of a phone number.
	-  **threads_tool.py**: run two jobs/codes on the same time.

  

## Installation

This repository supposed to be a package to PyPI. However, it has parts of code made by the classes of the instructor Bruno Dias. To maintain his credits, this repository will not be launched to PyPI.

## Usage

```python
from security_package.ping_kit.ping import ping_multiplo
from security_package.name_of_module.name_of_sub_module import function
```

  

## Author

Sarah Soares

This package was inspired on two courses of Digital Innovation One: **"Segurança da Informação com Python  "** with the Instructor Bruno Dias and **"Descomplicando a Criação de Pacotes de Processamento de Imagens em Python"** with the Instructor Karina Sato.

**Names of the Courses (English)**:
- Uncomplicated Creation of Image Processing Packages in Python with Karina Kato
- Information Security in Python with Bruno Dias.
  


## License

[MIT](https://choosealicense.com/licenses/mit/)
