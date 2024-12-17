""" A package to implement a minimal FHIR Terminology Service.
"""
import os
import sys
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s')
logger = logging.getLogger(__name__)

__version__ = "1.1.3"
__updated__ = '2024-08-17'
__url__ = 'https://medoco.health'
__author__ = 'Toni Magni'
__email__ = 'amagni@medoco.health'

DEFAULT_USER_TO_RUN_AS = ""
DEFAULT_VIRTUALENV_PATH = ""
DEFAULT_STARTINTERVAL = ""
DEFAULT_LISTEN = "127.0.0.1"
DEFAULT_PORT = 11112
DEFAULT_AET = "TOPS-DICOM"
DEFAULT_TOPSSERVER_USERNAME = "topsuser_ro"
DEFAULT_TOPSSERVER_SFTP_USERNAME = "topsserver"
DEFAULT_TOPSSERVER_SFTP_PORT = 22
DEFAULT_TOPSSERVER_SFTP_HOST = "topsserver"
SQLITE3_DB = "/var/lib/tops-dicom/tops-dicom.db"
PROGRAM_NAME = os.path.basename(sys.argv[0])
PROGRAM_VERSION = "v{}".format(__version__)
#    program_build_date = str(__updated__)
PROGRAM_VERSION_MESSAGE = '{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION)
PROGRAM_SHORTDESC = "DICOM Frontend SCP Server for topsServer."
PROGRAM_LICENSE = '''%s

  Created by %s on %s.
  Copyright 2024 Medoco Health. All rights reserved.
  
USAGE
''' % (PROGRAM_SHORTDESC, __author__, str(__updated__))

# Define the prefix used for the procedures to filter for as the ones to generate MWL from
MWL_PREFIX = u'\U0001F4F7'
