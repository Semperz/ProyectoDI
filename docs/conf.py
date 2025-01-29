# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

from sphinx.search import languages

sys.path.insert(0, os.path.abspath('E:\\Sergio\\DI\\Proyectos\\prietogarcia\\docs'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'prietogarcia'
copyright = '2025, Sergio Prieto Garcia'
author = 'Sergio Prieto Garcia'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [  'sphinx.ext.autodoc',
                'sphinx.ext.intersphinx',
                'sphinx.ext.ifconfig',
                'sphinx.ext.viewcode',
                'sphinx.ext.githubpages',
                ]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
source_suffix = '.rst'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
#html_static_path = ['_static']
