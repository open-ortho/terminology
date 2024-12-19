from typing import cast
import sys
import signal
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s')
from terminology.resources import Code, dentaleyepad, open_ortho, snomed

from sqlalchemy import and_
from topsserver_db.clinical import ProcedureTypeManager
from topsserver_db.models.topsdb import ProcedureType

# Used dynamically in the code via globals(). Do not remove.
from terminology.server.model import ScheduledProtocol, ScheduledProcedureStep

from terminology.server import logger, MWL_PREFIX
from terminology.server import verbosity_mapping
from terminology.server.model import ExternalProcedure, get_session, database_exists_and_valid, init_database
from terminology.server.args_cache import ArgsCache

def import_procedures(session, topsdb_config):
    args = ArgsCache.get_arguments()
    
    if not args.procedure_type_prefix:
        procedure_type_prefix = MWL_PREFIX
    else:
        procedure_type_prefix = args.procedure_type_prefix

    pmt = ProcedureTypeManager(config=topsdb_config)
    procedures = pmt.get_all_procedure_types_query().filter(
        and_(
            ProcedureType.short_label.startswith(procedure_type_prefix),
            ProcedureType.is_visible == True
        )
    )

    if not args.keep_procedures:
        logger.debug(f"Deleting all Existing External Procedures.")
        session.query(ExternalProcedure).delete()

    for procedure in procedures:
        if args.keep_procedures:
            existing_procedure = session.query(
                ExternalProcedure).filter_by(code=procedure.type_id).first()
            if existing_procedure:
                logger.debug(f"Modifying Existing Procedure {procedure.type_label}")
                existing_procedure.from_tops_procedure(procedure)
            else:
                ext = ExternalProcedure(tops_procedure=procedure)
                logger.debug(f"Adding New Procedure {procedure.type_label}")
                session.add(ext)
        else:
            ext = ExternalProcedure(tops_procedure=procedure)
            logger.debug(f"Adding New Procedure {procedure.type_label}")
            session.add(ext)


def import_terminology(session):
    """ Import codes into model.

    Designed to be a one-time or rarely used operation to do to import codes which can be used for MWL.  
    """
    logger.debug("Importing Terminology")
    codes = [] 
    def append_codes(modules):
        """ The codes coming from terminology don't have the name defined as text, but just as key name. This adds the key name as a field for code.
        """
        for module in modules:
            for name in dir(module):
                code = getattr(module, name)
                if isinstance(code, Code):
                    setattr(code, 'name', name)  # Dynamically add 'name' attribute
                    codes.append(code)

    append_codes([open_ortho, dentaleyepad, snomed])

    for code in codes:
        code = cast(Code, code)

        if code.contexts:
            # Process each context for the code
            for context in code.contexts:
                model_name = context.get("resource")

                # Dynamically get the model class based on model_name, skip if not found
                ModelClass = globals().get(model_name)
                if not ModelClass:
                    logger.debug(f"{ModelClass} is not a valid model.")
                    continue  # Skip if the model does not exist

                logger.debug(f"{ModelClass} is a valid model.")

                # Assuming each code has one context that defines the model name to use.
                model_name = code.contexts[0]["resource"]

                # Dynamically get the model class based on model_name. There has to be a model class with the exact same name as the context in the code.
                ModelClass = globals()[model_name]
    
                existing_model = session.query(ModelClass).filter_by(code_value=code.code).first()
    
                if existing_model:
                    existing_model.from_code(code, session)
                    logger.debug(f"Updating existing code {code.display}")
                else:
                    # Create an instance of the model using the model class dynamically determined.
                    existing_model = ModelClass()
                    existing_model.from_code(code, session)
                    session.add(existing_model)
                    logger.debug(f"Adding new code {code.display} into {ModelClass.__name__}")


def main():
    args = ArgsCache.get_arguments()

    level = verbosity_mapping.get(args.verbosity, logging.WARNING)
    logging.getLogger().setLevel(level)  # Set the root logger level
    logger.setLevel(level)
    logger.propagate = True
    logger.warning(f"effective level: {logger.getEffectiveLevel()}, LOG LEVEL: {level}, verbosity: {args.verbosity}")


    topsdb_config = {
        'username': args.topsserver_username,
        'password': args.topsserver_password,
        'host': args.topsserver_ip,
        'port': int(args.topsserver_port),
    }

    if not database_exists_and_valid():
        init_database()

    session = get_session()
    import_procedures(session,topsdb_config)
    import_terminology(session)
    session.commit()


def sigint_signal_handler(signal, frame):
    '''This will catch a SIGINT or ctrl-C and print what was done so far.'''
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_signal_handler)


if __name__ == "__main__":
    sys.exit(main())
