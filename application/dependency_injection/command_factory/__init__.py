from ....application import command as Command
from ....domain import repository as Repository

def get(repository: Repository) -> Command:
    return Command(repository)
