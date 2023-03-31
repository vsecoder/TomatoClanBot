from aiogram_dialog import DialogRegistry


def register_dialogs(registry: DialogRegistry):
    from . import starting_dialog

    registry.register(starting_dialog.ui)
