from ....application import result as Result
from .. import command_factory as CommandFactory
from .. import persistence_factory as PersistenceFactory
from .. import repository_factory as RepositoryFactory
from .. import resource_factory as ResourceFactory

def get() -> Result:
    persitence = PersistenceFactory.get()
    repository = RepositoryFactory.get(persitence)
    command = CommandFactory.get(repository)
    resource = ResourceFactory.get()

    return Result(command, resource)
