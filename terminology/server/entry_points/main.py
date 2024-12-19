"""The topsServer DICOM Listener

"""

import sys
import signal
import threading
from logging import DEBUG

from terminology.server import logger, PROGRAM_VERSION_MESSAGE
from terminology.server.entry_points import verbosity_mapping
from terminology.server.args_cache import ArgsCache
from terminology.server.fhir_api import app


def run_admin_gui():
    logger.info(f"{PROGRAM_VERSION_MESSAGE}: Request to start Web Configurator.")
    args = ArgsCache.get_arguments()
    from terminology.server.views.configurator_ui import flask_app
    debug = False
    if args.verbose == 2:
        debug = True
    flask_app.run(host=args.web_listen, port=int(args.web_port), debug=debug, use_reloader=False)

def run_fhir_api():
    import uvicorn
    *args, = ArgsCache.get_arguments()
    logger.info(f"{PROGRAM_VERSION_MESSAGE}: Request to start FHIR API.")
    uvicorn.run(app, host=args.fhir_listen, port=args.fhir_port)


def main():  # IGNORE:C0111
    args = ArgsCache.get_arguments()
    level = verbosity_mapping.get(args.verbose, DEBUG)
    logger.setLevel(level)
    logger.propagate = True

    logger.debug(("Logging Level is {}".format(
        logger.getEffectiveLevel())))

    if args.fhir_api and args.configurator_ui:
        # Thread for Flask
        flask_thread = threading.Thread(target=run_admin_gui)
        flask_thread.start()

        # Thread for FHIR API
        dicom_thread = threading.Thread(target=run_fhir_api)
        dicom_thread.start()

        flask_thread.join()
        dicom_thread.join()
    elif args.fhir_api:
        run_fhir_api()
    elif args.configurator_ui:
        run_admin_gui()


def sigint_signal_handler(signal, frame):
    '''This will catch a SIGINT or ctrl-C and print what was done so far.'''
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_signal_handler)


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''

    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


if __name__ == "__main__":
    sys.exit(main())
