import sys
import urllib
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

import requests

class BioParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.str = ""

  def handle_starttag(self, tag, attributes):
    if tag == 'li' and self.recording:
      self.str += '* '
    if tag != 'div':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'class' and value == 'wiki-content':
        break
    else:
      return
    self.recording = 1

  def handle_endtag(self, tag):
    if self.recording:
      if tag == 'div':
        self.recording -= 1
      if tag == 'br':
        self.str += '\n'
      if tag == 'p':
        self.str += '\n\n'

  def handle_data(self, data):
    if self.recording:
      self.str += data

  def handle_entityref(self, name):
    if self.recording:
      self.str += unichr(name2codepoint[name])

page = requests.get('http://last.fm/music/' + urllib.quote_plus(sys.argv[1]) + '/+wiki')

parser = BioParser()

parser.feed(page.text)

print parser.str.strip().encode('utf-8')
