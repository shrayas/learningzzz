#!/usr/bin/env python

import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section("user_details")
config.add_section("spreadsheet_details")
config.add_section("server_details")

config.set("user_details","username","")
config.set("user_details","password","")

config.set("spreadsheet_details","key","")
config.set("spreadsheet_details","worksheet","")

config.set("server_details","debug","")
config.set("server_details","port","")

with open("config.ini","w") as f:
    config.write(f)

print "done."
print "filename: config.ini"
