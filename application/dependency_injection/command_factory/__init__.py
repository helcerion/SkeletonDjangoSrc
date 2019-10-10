import application.command as Command
import domain.repository as Repository

def get(repository: Repository) -> Command:
    return Command(repository)
