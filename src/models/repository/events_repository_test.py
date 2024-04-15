import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo registro")
def test_insert_events():
    event = {
        "uuid": "idddd12312123233",
        "title": "Test Event123",
        "detail": "This is a test event",
        "slug": "test-event123",
        "maximum_attendees": 10,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)

    print(response)


def test_get_event_by_id():
    event_id = "idddd12312123233"

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)

    print(response)
