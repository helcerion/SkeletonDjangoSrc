import application.result as Result
import application.dependency_injection.command_factory as CommandFactory
import application.dependency_injection.persistence_factory as PersistenceFactory
import application.dependency_injection.repository_factory as RepositoryFactory
import application.dependency_injection.resource_factory as ResourceFactory

def get() -> Result:
    persitence = PersistenceFactory.get()
    repository = RepositoryFactory.get(persitence)
    command = CommandFactory.get(repository)
    resource = ResourceFactory.get()

    return Result(command, resource)
