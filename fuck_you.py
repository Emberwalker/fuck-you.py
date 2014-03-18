#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import sys
import psutil


# Static data
alpha = u" -_abcdefghijklmnopqrstuvwxyz1234567890"
flipped = u" -_ɐqɔpǝɟɓɥıɾʞlɯuodbɹsʇnʌʍxʎz⇂ᄅƐㄣގ9ㄥ860"

flip_dict = dict(zip(alpha, flipped))


# Functions
def killall(ps):
    for p in ps:
        p.terminate()
        p.kill()


def success(name):
    out = ''.join(flip_dict[a] for a in name)
    print(u"\n  (╯°□°）╯︵{}\n".format(out))


def main(*args):
    try:
        pname = args[-1].lower()
    except IndexError:
        print "Usage: {0} [you...] PROCESS_NAME".format(sys.argv[0])
        exit(-1)

    found = list()

    for process in psutil.process_iter():
        if process.name().lower() == pname:
            found.append(process)

    if not found:
        print(u"\n  (；￣Д￣) . o O( It’s not very effective... )\n")
        exit(-255)

    killall(found)
    success(pname)
    exit(0)

if __name__ == '__main__':
    main(*sys.argv[1:])
