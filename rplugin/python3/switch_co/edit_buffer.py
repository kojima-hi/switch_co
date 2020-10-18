#!/usr/bin/env python
# -*- coding: utf-8 -*-


def switch_commend(line, smbl='#'):
    if len(line) > 0:
        # strip CO for #
        if line[0] == smbl and line[1] != smbl:
            rev_line = line[1:]
        # add CO for not #
        elif line[0] != smbl:
            rev_line = smbl + line
        # not edit for ##
        else:
            rev_line = line
    return rev_line


def edit_buffer(buf, vblock_range):
    for i_line in range(vblock_range[0] - 1, vblock_range[1]):
        buf[i_line] = switch_commend(buf[i_line])
    return


def main(args_str=None):
    return


if __name__ == "__main__":
    main()
