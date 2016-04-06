# How to build the docs
# =====================
#
# First, install sphinx with markdown support and read-the-docs theme:
#
#     pip install sphinx sphinx-autobuild recommonmark sphinx_rtd_theme
#    
# Then run sphinx-build in the docs directory:
#
#     sphinx-build -b html docs docs/html
#

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import sphinx_rtd_theme
import os

# Enable Read-the-Docs theme locally
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Enable Markdown support for documentation
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

copyright = u"S. Astanin 2016"

# Enable automatic TOC generation
def setup(app):
    app.add_config_value('recommonmark_config', {
            'enable_auto_toc_tree': True,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)