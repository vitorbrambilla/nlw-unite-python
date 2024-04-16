import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo registro")
def test_insert_attendee():
    event_id = 'idddd12312123233'

    attendees_info = {
        'uuid': 'meu_uuid',
        'name': 'Test Attendee',
        'email': 'email@email.com',
        'event_id': event_id
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)

    print(response)


def test_get_attendee_badge_by_id():
    attendee_id = 'meu_uuid'

    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(response)
