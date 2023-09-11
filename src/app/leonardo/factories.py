import uuid
from datetime import datetime, timedelta

import factory.fuzzy
from dateutil import tz

DATETIME_NOW = datetime.now(tz=tz.UTC)


class LegAvailabilityHistoryFactory(factory.DictFactory):
    uid = factory.LazyFunction(uuid.uuid4)
    legId = factory.LazyFunction(uuid.uuid4)
    available = factory.fuzzy.FuzzyInteger(999)
    booked = factory.fuzzy.FuzzyInteger(999)
    waitlist = factory.fuzzy.FuzzyInteger(999)
    state = factory.fuzzy.FuzzyText(length=4)
    updated = factory.fuzzy.FuzzyDateTime(
        DATETIME_NOW - timedelta(days=100), DATETIME_NOW
    )


class CabinAvailabilityHistoryFactory(factory.DictFactory):
    uid = factory.LazyFunction(uuid.uuid4)
    code = factory.fuzzy.FuzzyText(length=1)
    available = factory.fuzzy.FuzzyInteger(999)
    booked = factory.fuzzy.FuzzyInteger(999)
    waitlist = factory.fuzzy.FuzzyInteger(999)


class SubclassAvailabilityHistoryFactory(factory.DictFactory):
    uid = factory.LazyFunction(uuid.uuid4)
    state = factory.fuzzy.FuzzyText(length=4)
    code = factory.fuzzy.FuzzyText(length=1)
    available = factory.fuzzy.FuzzyInteger(999)
    booked = factory.fuzzy.FuzzyInteger(999)
    waitlist = factory.fuzzy.FuzzyInteger(999)
