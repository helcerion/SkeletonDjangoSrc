from ....domain import repository as Repository
from ....infrastructure import persistence as Persistence

def get(persistence: Persistence) -> Repository:
    return Repository(persistence)
