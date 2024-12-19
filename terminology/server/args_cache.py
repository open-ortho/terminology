""" Configuration and variables.

Class to get options from env variables.

Argparse support was purposely removed, because it was creating too much trouble with unittests, and too much overhead. Arguments can be just as easily passed as env vars, and since this is a server, not a tool to be used every day, arguments should not be necessary anyways.

"""
import os
from distutils.util import strtobool
from terminology.server import * 


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ArgsCache:
    _args = None

    @staticmethod
    def get_arguments(test_args=None):
        if test_args is not None:
            return Namespace(**test_args)
        if ArgsCache._args is None:
            ArgsCache._args = ArgsCache.load_arguments()
        return ArgsCache._args

    @staticmethod
    def load_arguments():
        # Create an object similar to argparse.Namespace
        return Namespace(
            # The path of the SQLite DB file for the local mapping.
            database_file=os.getenv('OT_DATABASE_FILE', SQLITE3_DB),

            # Needs to be set to True for the /admin web server (configurator UI) to run.
            configurator_ui=bool(
                strtobool(os.getenv('OT_CONFIGURATOR_UI', 'False'))),

            # The secret key required for Flask to run properly (used for configurator UI)
            flask_secret_key=os.getenv('OT_FLASK_SECRET_KEY', None),

            # IP and port for the Flask configurator UI server.
            web_listen=os.getenv('OT_WEB_LISTEN', '0.0.0.0'),
            web_port=os.getenv('OT_WEB_PORT', '5000'),
        
            # FHIR API server IP and port.
            fhir_listen=os.getenv('OT_FHIR_LISTEN', ''),
            fhir_port=os.getenv('OT_FHIR_PORT', '8000'),
        )
