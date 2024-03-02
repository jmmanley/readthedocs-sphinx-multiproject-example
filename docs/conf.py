# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# -- General configuration ---------------------------------------------------
#
# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
# RJG - This file is set up to allow the sphinx-multiproject to build the docs for align, view and edit from a single repository
extensions = [
   "multiproject",
]

# Define the projects that will share this configuration file.
# These have to match the project environmental variable defined in the readthedocs admin menu (readthedocs project --> admin --> environmental variables; i.e.SPIERSalign/docs,SPIERSedit/docs or SPIERSview/docs)
multiproject_projects = {
    "package1": {
         "config": {
            "project": "package1",
            "html_title": "package1",
            "path":  "package1/",
         },
    },
    "package2": {
         "config": {
            "project": "package2",
            "html_title": "package2",
            "path":  "package2/",
         },
    },
}