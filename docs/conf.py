import os
import sys
import sphinx_bootstrap_theme
sys.path.append(os.path.abspath(".."))
import bot

master_doc = "index"
project = bot.__title__
copyright = bot.__copyright__
version = bot.__version__
language = "es"
html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = "img/logo.png"
html_theme_options = {"bootswatch_theme": "united"}
