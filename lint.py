#!/usr/bin/env python3

"""Lint the index.yaml file as well as all files ending with .mixin."""

import os
import sys

try:
    from yamllint.cli import run
except ImportError:
    sys.exit("Failed to import Python package 'yamllint'")

any_error = False
for name in sorted(os.listdir()):
    if name != 'index.yaml' and not name.endswith('.mixin'):
        continue

    try:
        run([
            '--config-data',
            '{'
            'extends: default, '
            'rules: {'
            'document-start: {present: false}, '
            'empty-lines: {max: 0}, '
            'key-ordering: {}, '
            'line-length: {max: 999}'
            '}'
            '}',
            '--strict',
            name,
        ])
    except SystemExit as e:
        any_error |= bool(e.code)
        continue
    assert False, 'run() should always raise SystemExit'

sys.exit(1 if any_error else 0)
