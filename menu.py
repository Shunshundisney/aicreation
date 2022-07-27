#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import codecs

form = cgi.FieldStorage()


html = codecs.open('/Users/tanakashunta/MUDS/人工知能アルゴリズム/last/html/view.html', 'r', 'utf-8').read()

print("")
print(html)