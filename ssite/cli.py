# Copyright 2018, The Ssite Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import argparse
import sys

from . import index
from . import clean
from . import rmblock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(title='commands', dest='command')

    index_parser = subparsers.add_parser(
        'index', help=index.__doc__)
    index.add_cli_args(index_parser)

    clean_parser = subparsers.add_parser(
        'clean', help=clean.__doc__)
    clean.add_cli_args(clean_parser)

    rmblock_parser = subparsers.add_parser(
        'beta_rmblock', help=rmblock.__doc__)
    rmblock.add_cli_args(rmblock_parser)

    args = parser.parse_args()
    if args.command == 'clean':
        clean.main(args)
    elif args.command == 'index':
        index.main(args)
    elif args.command == 'beta_rmblock':
        rmblock.main(args)
    else:
        print(
            'Got unknown command "{}".'.format(args.command),
            file=sys.stderr)
        parser.print_help()
