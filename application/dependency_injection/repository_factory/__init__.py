import domain.repository as Repository
import infrastructure.persistence as Persistence

def get(persistence: Persistence) -> Repository:
    return Repository(persistence)
