#!/usr/bin/python
#
#
import os
import sys
import ansi

header = ansi.escapes.HEADER
blue = ansi.escapes.OKBLUE
green = ansi.escapes.OKGREEN
warning = ansi.escapes.WARNING
fail = ansi.escapes.FAIL
endc = ansi.escapes.ENDC
bold = ansi.escapes.BOLD
underline = ansi.escapes.UNDERLINE


print warning + "\n[!]...Checking for latest Update, Please Wait..." + endc

os.system("git pull ")

cont = raw_input(green + "\n[!]...Update Finished, \n\nPress 'Return' to Continue: " + endc)

import raspn3t










