#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='flajt',
      version='0.0.1',
      description='Renders flysight recordings',
      author=u'Björn Edström',
      author_email='be@bjrn.se',
      url='https://github.com/bjornedstrom/flajt',
      scripts=['bin/flajt'],
      data_files=[('/usr/share/flajt/web', [
                'web/index.html',
                'web/view.html',
                ])]
     )
