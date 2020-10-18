#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynvim as vim
import pyperclip
from switch_co.util import get_vblock_range, get_buffer
from switch_co.edit_buffer import edit_buffer


@vim.plugin
class SwitchCommendOut(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @vim.command("SwitchCO", range='', nargs='*')
    def switch_commend_out(self, args, rng):
        buf = get_buffer(self.nvim)
        vblock_range = get_vblock_range(self.nvim)

        edit_buffer(buf, vblock_range)


