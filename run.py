#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# The MIT License (MIT)

# Copyright (c) 2014 Zhassulan Zhussupov

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from optparse import OptionParser
from iconfinder_api import IconfinderAPI

my_api_key = 'Your API key'

usage = "%prog [options]\n\n"
usage += "Command-line tool for downloading icons from https://www.iconfinder.com\n"
usage += "Copyright (c) 2014 Zhussupov Zhassulan zhzhussupovkz@gmail.com\n"
usage += "While using this program, get API key from https://www.iconfinder.com"
option_parser = OptionParser(usage=usage, version="%prog 1.0")
option_parser.add_option("-q", "--query", help = "search for icons by search term", default = "python")
option_parser.add_option("-d", "--dir", help = "folder, which will be downloaded icons", default = "icons")
option_parser.add_option("-p", "--page", help = "specify result page(index). starts from 0", default = 0)
option_parser.add_option("-c", "--count", help = "number of icons per page", default = 10)
option_parser.add_option("-i", "--min", help = "specify minimum size of icons", default = 1)
option_parser.add_option("-x", "--max", help = "specify maximum size of icons", default = 48)
(options, args) = option_parser.parse_args()

api = IconfinderAPI(my_api_key)
api.download(dir = options.dir, q = options.query, p = options.page, c = options.count, min = options.min, max = options.max)
