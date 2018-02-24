#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  f = open(filename, 'rU')

  yr = re.search(r'(\d+)</h3>',f.read())
  if yr: year = yr.group(1)
  else: year = 'Unknown'

  f.seek(0)
  filedata = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())

  namesdict = {}

  for i in filedata:
      girlname = i[2] 
      boyname = i[1]
      rank = i[0]

      if girlname in namesdict.keys():
          oldrank = namesdict[girlname]

          if oldrank > rank: newrank = rank
          else: newrank = oldrank

          namesdict[girlname] = newrank
 
      else:
          namesdict[girlname] = rank

      if boyname in namesdict.keys():
          oldrank = namesdict[boyname]

          if oldrank > rank: newrank = rank
          else: newrank = oldrank

          namesdict[boyname] = newrank
 
      else:
          namesdict[boyname] = rank

  namelist = []
  namelist.append(year)

  for j in sorted(namesdict.keys()):
      namerank = j + ' ' + namesdict[j]
      namelist.append(namerank)

  f.close()

  return(namelist)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:

      namelist = extract_names(filename)
 
      if summary == False: 
         for name in namelist: print name
      else:
         summaryfile = filename.replace('html','html.summary')  
         g = open(summaryfile,'w')
         for name in namelist: 
             line = name + '\n'
             g.write(line)
  
if __name__ == '__main__':
  main()
