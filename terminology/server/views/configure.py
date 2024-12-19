from typing import cast
import npyscreen
from sqlalchemy.orm import Session

from server.args_cache import ArgsCache
from server.model import ExternalProcedure, RequestedProcedure, ScheduledProcedureStep, ScheduledProtocol, get_session, get_engine

engine = None
session = None

MAIN = 'MAIN'
EXTERNAL_PROCEDURES = 'EXTERNAL_PROCEDURES'
REQUESTED_PROCEDURES = 'REQUESTED_PROCEDURES'
SCHEDULED_STEPS = 'SCHEDULED_STEPS'
SCHEDULED_PROTOCOLS = 'SCHEDULED_PROTOCOLS'


class MainForm(npyscreen.ActionForm):
    def create(self):
        self.menu = self.add(npyscreen.TitleSelectOne, max_height=4, value=[0],
                             name="Main Menu", values=["External Procedures", "Requested Procedures", "Scheduled Steps", "Scheduled Protocols"],
                             scroll_exit=True)

    def afterEditing(self):
        pass

    def on_ok(self):
        choice = self.menu.get_selected_objects()[0]
        if choice == "External Procedures":
            self.parentApp.switchForm(EXTERNAL_PROCEDURES)
        elif choice == "Requested Procedures":
            self.parentApp.switchForm(REQUESTED_PROCEDURES)
        elif choice == "Scheduled Steps":
            self.parentApp.switchForm(SCHEDULED_STEPS)
        elif choice == "Scheduled Protocols":
            self.parentApp.switchForm(SCHEDULED_PROTOCOLS)
        else:
            self.parentApp.switchForm(None)

    def on_cancel(self):
        self.parentApp.switchForm(None)


class BaseForm(npyscreen.ActionForm):
    def create(self):
        self.add_nav_buttons()

    def add_nav_buttons(self):
        self.main_btn = self.add(
            npyscreen.ButtonPress,
            name="Go to External Procedures",
            when_pressed_function=self.go_external_procedure)
        self.requested_procedure_btn = self.add(
            npyscreen.ButtonPress, name="Go to Requested Procedures", when_pressed_function=self.go_requested_procedures)
        self.scheduled_steps_btn = self.add(
            npyscreen.ButtonPress, name="Go to Scheduled Steps", when_pressed_function=self.go_scheduled_steps)
        self.scheduled_protocols_btn = self.add(
            npyscreen.ButtonPress, name="Go to Scheduled Protocols", when_pressed_function=self.go_scheduled_protocols)

    def go_external_procedure(self):
        self.parentApp.switchForm(EXTERNAL_PROCEDURES)

    def go_requested_procedures(self):
        self.parentApp.switchForm(REQUESTED_PROCEDURES)

    def go_scheduled_steps(self):
        self.parentApp.switchForm(SCHEDULED_STEPS)

    def go_scheduled_protocols(self):
        self.parentApp.switchForm(SCHEDULED_PROTOCOLS)

    def on_ok(self):
        # Default OK behavior, can be overridden
        self.parentApp.switchForm(MAIN)

    def on_cancel(self):
        session.rollback()
        self.parentApp.switchFormPrevious()


class ExternalProceduresForm(BaseForm):
    def create(self):
        super().create()  # Calls create method of BaseForm to add navigation buttons
        self.procedure_list = self.add(
            npyscreen.TitleSelectOne,
            max_height=20,
            name="Pick External Procedure",
            values=["List External Procedures here..."],
            scroll_exit=True,
            check_value_change=True)
        # Fields for editing procedure details
        self.name = self.add(npyscreen.TitleText, name="Name:")
        self.system = self.add(npyscreen.TitleText, name="System:")
        self.code = self.add(npyscreen.TitleText, name="Code:")
        self.name = self.add(npyscreen.TitleText, name="Name:")
        self.short_name = self.add(npyscreen.TitleText, name="Short Name:")

    def beforeEditing(self):
        # Fetch procedures from database
        self.procedures = session.query(ExternalProcedure).all()
        self.procedure_list.values = [p.name for p in self.procedures]
        self.update_fields()

    def when_value_edited(self):
        self.update_fields()

    def update_fields(self):
        # Populate form fields with the details of the selected procedure
        selected_index = self.procedure_list.value[0] if self.procedure_list.value else 0
        if selected_index is not None:
            selected_procedure = self.procedures[selected_index]
            selected_procedure = cast(ExternalProcedure, selected_procedure)
            self.name.value = selected_procedure.name
            self.system.value = selected_procedure.system
            self.code.value = selected_procedure.code
            self.name.value = selected_procedure.name
            self.short_name.value = selected_procedure.short_name
            self.display()

    def on_ok(self):
        # Save changes to the selected procedure
        self.update_fields()
        selected_index = self.procedure_list.value[0] if self.procedure_list.value else None
        if selected_index is not None:
            selected_procedure = session.query(
                ExternalProcedure).all()[selected_index]
            selected_procedure.name = self.name.value
            selected_procedure.system = self.system.value
            selected_procedure.code = self.code.value
            selected_procedure.name = self.name.value
            selected_procedure.short_name = self.short_name.value
            session.commit()
        npyscreen.notify_confirm("External Procedure updated.")


class RequestedProceduresForm(BaseForm):
    def create(self):
        super().create()  # Add common buttons
        self.name = self.add(npyscreen.TitleText, name="Name:")
        self.name = self.add(npyscreen.TitleText, name="Name:")
        self.procedure_list = self.add(npyscreen.TitleMultiSelect, max_height=None,
                                       name="Pick Requested Procedure", values=["List External Procedures here..."])
        # Further custom widgets

    def beforeEditing(self):
        procedures = session.query(RequestedProcedure).all()
        self.procedure_list.values = [p.code_meaning for p in procedures]
        session.close()


class ScheduledProcedureStepsForm(BaseForm):
    def create(self):
        super().create()
        self.step_name = self.add(npyscreen.TitleText, name="Step Name:")
        self.procedure_list = self.add(npyscreen.TitleMultiSelect, max_height=None,
                                       name="Pick Scheduled Procedure Step", values=["List External Procedures here..."])
        # Further specific widgets

    def beforeEditing(self):
        procedures = session.query(ScheduledProcedureStep).all()
        self.procedure_list.values = [p.code_meaning for p in procedures]
        session.close()


class ScheduledProtocolsForm(BaseForm):
    def create(self):
        super().create()
        self.step_name = self.add(npyscreen.TitleText, name="Step Name:")
        self.protocols_list = self.add(npyscreen.TitleMultiSelect, max_height=None,
                                       name="Pick Scheduled Protocols", values=["List External Procedures here..."])
        # Further specific widgets

    def beforeEditing(self):
        procedures = session.query(ScheduledProtocol).all()
        self.protocols_list.values = [p.code_meaning for p in procedures]
        session.close()


class TopsDicomConfigure(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm(MAIN, MainForm, name='Main Menu')
        self.addForm(EXTERNAL_PROCEDURES, ExternalProceduresForm,
                     name='External Procedures')
        self.addForm(REQUESTED_PROCEDURES, RequestedProceduresForm,
                     name='Requested Procedures')
        self.addForm(SCHEDULED_STEPS, ScheduledProcedureStepsForm,
                     name='Scheduled Procedure Steps')
        self.addForm(SCHEDULED_PROTOCOLS, ScheduledProtocolsForm,
                     name='Scheduled Protocols')

        self.addForm(EXTERNAL_PROCEDURES, ExternalProceduresForm,
                     name='External Procedures')
        self.addForm(REQUESTED_PROCEDURES,
                     RequestedProceduresForm, name='Requested Procedures')
        self.addForm(SCHEDULED_STEPS, ScheduledProcedureStepsForm,
                     name='Scheduled Procedure Steps')
        self.addForm(SCHEDULED_PROTOCOLS,
                     ScheduledProtocolsForm, name='Scheduled Protocols')

    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")

    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()


if __name__ == '__main__':
    args = ArgsCache.get_arguments()
    engine = get_engine()
    session = get_session(engine)
    app = TopsDicomConfigure().run()
