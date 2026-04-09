"""
Get configuration options.
"""

import argparse
import sys

import edq.core.argparser

def run_cli(args):
    """ run the CLI."""

    config_info = args._config_info

    config = config_info.config
    if (args.scope_local):
        config = edq.util.json.load_path(config_info.local_config_path)

    if (args.scope_global):
        config = edq.util.json.load_path(config_info.global_config_path)

    if (args.scope_file is not None):
        config = edq.util.json.load_path(args.scope_file)

    rows = []
    for key in args.config_to_get:
        value = config.get(key, None)
        if (value is not None):
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
    modify_parser(parser)
    return parser

def modify_parser(parser: argparse.ArgumentParser) -> None:
    """ Add this CLI's flags to the given parser. """

    parser.add_argument('config_to_get', metavar = "KEY",
        action = 'store', nargs = '+', type = str,
        help = ("Configuration key to get."),
    )

    edq.core.config.add_config_display_arguments(parser)
    edq.core.config.add_config_location_argument_group(parser)

if (__name__ == '__main__'):
    sys.exit(main())
