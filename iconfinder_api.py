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

import urllib
import urllib2
import json
import base64
import os

class IconfinderAPI:

	def __init__(self, api_key):
		self.api_key = api_key
		self.api_url = 'https://www.iconfinder.com/json/'

	# send request
	def send_request(self, api_method, query_args):
		required_args = {'api_key' : self.api_key }
		query_args.update(required_args)
		query_args = urllib.urlencode(query_args)
		url = self.api_url + api_method + '/?' + query_args
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		try:
			page = json.loads(resp.read())
			resp.close()
			return page
		except:
			resp.close()
			return False

	# search icons
	def search(self, q = 'icon', p = 0, c = 10, min = 1, max = 48):
		query_args = {'q' : q, 'p' : p, 'c' : c, 'min' : min, 'max' : max }
		params = {'l' : 0, 'price' : 'any' }
		query_args.update(params)
		json = self.send_request('search', query_args)
		if json:
			return json.get('searchresults').get('icons')

	# get icon details
	def icondetails(self, id = 1, size = 128):
		query_args = {'id' : id, 'size' : size }
		json = self.send_request('icondetails', query_args)
		if json:
			return json.get('icon')

	# download icons by search query
	def download(self, q = 'icon', p = 0, c = 10, min = 1, max = 48):
		icons = self.search(q, p, c, min, max)
		print "Found %s icons for search query: %s" % (len(icons), q)
		try:
			for icon in icons:
				link = icon.get('image')
				resp = urllib2.urlopen(link)
				filename = link.split('/')[-1]
				f = open(filename, "wb")
				f.write(resp.read())
				f.close()
				print "Icon %s: OK" % filename
		except:
			print "Error when downloading icons"
