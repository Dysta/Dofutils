# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Dofutils"
copyright = "2023, Dysta"
author = "Dysta"
release = "0.0.4"

sys.path.insert(0, os.path.abspath(".."))
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autosummary_generate = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_material"
html_theme_options = {
    "repo_url": "https://github.com/Dysta/Dofutils",
    "repo_name": "Dofutils",
    "nav_title": "Dofutils",
    "color_primary": "teal",
    "theme_color": "97a800",
}
html_static_path = ["_static"]
