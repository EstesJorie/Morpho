# Morpho Toolkit

<p align="center">
    <picture>
      <source srcset="images/MORPHO_dev_header.png" media="(prefers-color-scheme: light)">
      <source srcset="images/MORPHO_dev_light_header.png" media="(prefers-color-scheme: dark)">
      <img src="images/morpho_logo_one.png" alt="Morpho Logo" width="50%">
    </picture>
</p>

This is the DEV version of the Morpho toolkit in which some files or processes might still be work-in-progress. 
For the most stable version of the toolkit, please clone the main branch of the toolkit.

 Welcome to the Morpho toolkit. The Morpho toolkit is designed to streamline and
 speedup your data science workflow. The toolkit features numerous "template" files
 designed to be imported into your current file which then allows you to access
 various functions encapsulating the data science pipeline.
 
 ## Cloning/Installation 
 
 To clone the repository, type into your terminal:
 
 > git clone https://github.com/EstesJorie/Morpho.git

## Dependency Installation

- PIP
To install all of the required dependecies, type into your terminal:

> pip install -r requirements.txt

- CONDA
There are two options for dependcy installation for Conda, the first involves activating the provided .yml file, the second involves creating your own environment with pip and then installing the required dependecies. To activate the provided .yml environment, enter:

> conda env create -f environment.yml
> conda activate MORPHO

For PIP, type the following commands into your terminal:

> conda create --name [name] python=3.[ver]
> conda activate [envname]
> conda install pip
> pip install -r requirements.txt
