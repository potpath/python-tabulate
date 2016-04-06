# Overview

Tabulate is a a Python library and a command-line utility to pretty-print
tabular data.

 * [Overview](index.md)
 * [Installation](install.md)
 * [Input data types](inputtypes.md)
 * [Output formats](tableformats.md)
 * [Command line utility](commandline.md)


## For Python Programmers

Tabulate is designed to print small tables easily:

 - there is just [one function to call](api.md), `tabulate()`
 - it may take many [tabular data types](inputtypes.md) as input 
 - the output layout is data-driven

Tabulate creates a readable presentation of mixed textual
and numeric data

 - textual and numeric columns are aligned automatically
 - numbers can be aligned by a decimal point
 - numbers' format is configurable

Tabulate may be used to author tabular data for lightweight
plain-text markup:

 - Markdown
 - ReStructuredText
 - org-mode
 - MediaWiki
 - MoinMoin
 - LaTeX
 - and some other [output formats](tableformats.md) are supported.

Tabulate is a single-file library distributed under MIT license.
It can be easily bundled with other projects.


## For Non-Programmers

Non-programmers may use the [command line utility](commandline.md)
to pretty-print tabular data from a plain-text file.
