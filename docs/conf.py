# Configuration file for the Sphinx documentation builder.

import os
import sys
from sphinx_needs import __version__
print ('sphinx-needs version: ' + str(__version__))
from sphinx_needs.api import add_dynamic_function

sys.path.append(os.path.abspath('.'))
import metamodel

# -- For autodoc

# For test:
sys.path.append(os.path.abspath('../tests'))
import test_ai_interaction

# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'GPT Evaluation'
copyright = f'2025 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.0'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx_needs',
    'sphinx.ext.autodoc',
    'sphinxcontrib.test_reports',
    #'sphinxcontrib.plantuml',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx_immaterial'
#html_theme = 'alabaster' # Sphinx Defaul Theme

# If we do perform a PDF build, we have to switch to alabaster
if os.environ.get("PDF", 0) == 1:
    html_theme = 'alabaster' # Sphinx Defaul Theme

#html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

print('plantuml path: ' + str(plantuml))

plantuml_output_format = 'svg'

# sphinx_needs configuration

needs_role_need_max_title_length = -1

needs_build_json = True

needs_id_regex = metamodel.needs_id_regex

needs_types = metamodel.needs_types

needs_extra_options = metamodel.needs_extra_options

needs_extra_links = metamodel.needs_extra_links

needs_services = metamodel.needs_services

needs_layouts = metamodel.needs_layouts

needs_global_options = metamodel.needs_global_options

needs_render_context = metamodel.needs_render_context

needs_warnings = metamodel.needs_warnings

needs_string_links = metamodel.needs_string_links

def setup(app):

    for func in metamodel.needs_functions:
        add_dynamic_function(app, func)
