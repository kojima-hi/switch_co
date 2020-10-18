#!/usr/bin/env python
# -*- coding: utf-8 -*-


def echo(vim, msg):
    vim.command("echo '" + msg + "'")
    return


def get_buffer(vim):
    return vim.current.buffer


def get_vblock_range(vim):
    sta_line = vim.eval("getpos(\"'<\")")[1]
    end_line = vim.eval("getpos(\"'>\")")[1]
    return [sta_line, end_line]


def main(args_str=None):
    return


if __name__ == "__main__":
    main()
