"""
List the current configuration options.
"""

import argparse
import sys

import edq.core.argparser
import edq.core.config

def run_cli(args: argparse.Namespace) -> int:
    """ Run the CLI. """

    config_info = args._config_info

    rows = []
    for (key, value) in config_info.config.items():
        row = [key, str(value)]
        edq.core.config.add_origin(row, config_info, args.show_origin, key)
        rows.append(edq.core.config.CONFIG_FIELD_SEPARATOR.join(row))

    rows.sort()

    edq.core.config.add_header(
        rows,
        args.skip_header,
        args.show_origin,
    )

    print("\n".join(rows))
    return 0

def main() -> int:
    """ Get a parser, parse the args, and call run. """

    return run_cli(_get_parser().parse_args())

def _get_parser() -> argparse.ArgumentParser:
    """ Get a parser and add addition flags. """

    parser = edq.core.argparser.get_default_parser(__doc__.strip())
    edq.core.config.add_config_display_arguments(parser)

    return parser

if (__name__ == '__main__'):
    sys.exit(main())
