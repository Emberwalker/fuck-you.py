#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import sys
import psutil


# Static data
alpha = u" -_abcdefghijklmnopqrstuvwxyz1234567890"
flipped = u" -_ɐqɔpǝɟɓɥıɾʞlɯuodbɹsʇnʌʍxʎz⇂ᄅƐㄣގ9ㄥ860"


# Functions
def killall(ps):
    for p in ps:
        p.terminate()
        p.kill()


def success(name):
    out = u""
    for i in range(0, len(name)):
        out += flipped[alpha.index(name[i])]

    print(u"\n  (╯°□°）╯︵{}\n".format(out))


# Main
if len(sys.argv) is 1:
    print "Usage: {0} [you...] PROCESS_NAME".format(sys.argv[0])
    exit(-1)

pname = sys.argv[len(sys.argv) - 1].lower()
found = list()

for process in psutil.process_iter():
    if process.name().lower() == pname:
        found.append(process)

if len(found) is 0:
    print(u"\n  (；￣Д￣) . o O( It’s not very effective... )\n")
    exit(-255)

killall(found)
success(pname)
exit(0)