
import git

from git_contributions_importer import *

repo1 = git.Repo("/Users/tianahorn/coding/getJusticeMobile/getjustice")


# Mock Repo
mock_repo = git.Repo("/Users/tianahorn/coding/PrivateRepoMock/Private-Repo")

importer = Importer([repo1], mock_repo)

#importer.set_author(['tiana.horn@gmail.com','tiana@flowerchildremedies.com'])

importer.import_repository()