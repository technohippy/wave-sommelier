#!/usr/bin/env python

import os
import logging
import wsgiref.handlers
from extension import Extension
from data import StoreData

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, {}))

class SearchHandler(webapp.RequestHandler):
  def get(self):
    keywords = self.request.get('keywords').split(' ')
    apis = self.request.get('apis')
    if apis:
      apis = apis.split(',')
    else:
      apis = []
    langs = self.request.get('langs')
    if langs:
      langs = langs.split(',')
    else:
      langs = []

    q = Extension.all()
    #if apis: q.filter("apis IN", apis.split(','))
    #if langs: q.filter("langs IN", apis.split(','))
    all_extensions = q.fetch(200)
    extensions = []
    for e in all_extensions:
      key_found = True
      for keyword in keywords:
        if 0 <= e.desc.find(keyword) or 0 <= e.techDesc.find(keyword) or 0 <= e.title.find(keyword):
          key_found = key_found or True
        else:
          key_found = False

      api_found = False
      for api in apis:
        if api in e.apis:
          api_found = True

      lang_found = False
      for lang in langs:
        if lang in e.langs:
          lang_found = True

      if key_found and api_found and lang_found:
        extensions.append(e)

    if len(extensions) == 0:
      self.response.out.write('No Data')
    else:
      path = os.path.join(os.path.dirname(__file__), 'search.html')
      self.response.out.write(template.render(path, {'extensions': extensions[:10]}))

class InitializeHandler(webapp.RequestHandler):
  def get(self):
    """
    q = Extension.all()
    extensions = q.fetch(200)
    db.delete(extensions)
    StoreData()
    self.response.out.write('Done')
    """
    self.response.out.write('ignore')

def main():
  application = webapp.WSGIApplication(
    [
      ('/', MainHandler),
      ('/search', SearchHandler),
      ('/initialize', InitializeHandler)
    ],
    debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
