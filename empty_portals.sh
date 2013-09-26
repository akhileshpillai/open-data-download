#!/bin/sh
ls -l portals/ckan|sed -e 's/^.*users//' -e 's/[A-Z][a-z][a-z] [0-9 ][0-9] [0-9][0-9]:[0-9][0-9]//'
