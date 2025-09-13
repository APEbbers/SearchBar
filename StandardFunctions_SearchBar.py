def ReturnXML_Value(
    path: str, ElementName: str, attribKey: str = "", attribValue: str = ""
):
    import xml.etree.ElementTree as ET
    import os

    # Passing the path of the
    # xml document to enable the
    # parsing process
    PackageXML = os.path.join(os.path.dirname(__file__), path)
    tree = ET.parse(PackageXML)
    # getting the parent tag of
    # the xml document
    root = tree.getroot()
    result = ""
    for child in root:
        if str(child.tag).split("}")[1] == ElementName:
            if attribKey != "" and attribValue != "":
                for key, value in child.attrib.items():
                    if key == attribKey and value == attribValue:
                        result = child.text
                        return result
            else:
                result = child.text
    return result


def ReturnXML_Value_Git(
    User="APEbbers",
    Repository="FreeCAD-Ribbon",
    Branch="main",
    File="package.xml",
    ElementName: str = "",
    attribKey: str = "",
    attribValue: str = "",
    host="https://codeberg.org/",
):
    import requests_local as requests
    import xml.etree.ElementTree as ET

    result = None
    try:
        if host.endswith("/") is False:
            host = host + "/"
        
        # Passing the path of the
        # xml document to enable the
        # parsing process
        url = f"{host}/{User}/{Repository}/{Branch}/{File}"
        response = requests.get(url)
        data = response.content
        root = ET.fromstring(data)
        result = ""
        for child in root:
            if str(child.tag).split("}")[1] == ElementName:
                if attribKey != "" and attribValue != "":
                    for key, value in child.attrib.items():
                        if key == attribKey and value == attribValue:
                            result = child.text
                            return result
                else:
                    result = child.text
    except Exception:
        pass
    return result


def GetGitData(PrintErrors=False):
    GitInstalled = True
    import os

    try:
        import git
    except ImportError:
        GitInstalled = False

    commit = None
    branch = None
    Contributers = []
    result = [commit, branch, Contributers]

    git_root = os.path.join(os.path.dirname(__file__), ".git")
    if os.path.exists(git_root) is False:
        return result
    git_head = os.path.join(git_root, "HEAD")
    if os.path.exists(git_head) is False:
        return result

    # Read .git/HEAD file
    with open(git_head, "r") as fd:
        head_ref = fd.read()

    # Find head file .git/HEAD (e.g. ref: ref/heads/master => .git/ref/heads/master)
    if not head_ref.startswith("ref: ") and PrintErrors is True:
        print(f"expected 'ref: path/to/head' in {git_head}")
        return result
    head_ref = head_ref[5:].strip()

    # Read commit id from head file
    head_path = os.path.join(git_root, head_ref)
    if os.path.exists(head_path) is False and PrintErrors is True:
        print(f"path {head_path} referenced from {git_head} does not exist")
        return result
    # Read the branch version
    branch = head_path.rsplit("/", 1)[1]
    with open(head_path, "r") as fd:
        line = fd.readlines()[0]
        commit = line.strip()

    # If gitpython is installed, get the list of contributors
    if GitInstalled is True:
        repo = git.Repo(git_root)
        Git = repo.git
        List = Git.execute(
            ["git", "shortlog", "-sn", "-e", "--all"],
            as_process=False,
            stdout_as_string=True,
        )
        UserList = []
        for line in List.splitlines():
            Commits = str(line)[: len("  1418  ") - 1]
            Commits = int(Commits.strip())
            User = str(line)[len("  1418  ") - 1 :].split("<")[0].strip()
            email = (
                str(line)[len("  1418  ") - 1 :].split("<")[1].replace(">", "").strip()
            )

            UserList.append([Commits, User, email])

        tempList = []
        for i in range(len(UserList) - 1):
            User = UserList[i]
            if User[1] not in Contributers and User[1] != "pre-commit-ci[bot]":
                Contributers.append(User[1])
                tempList.append(User)
            if User[1] in Contributers:
                for j in range(len(UserList) - 1):
                    tempUser = UserList[j]
                    if tempUser[2] == User[2] and tempUser[0] > User[0]:
                        Contributers.pop()
                        if (
                            tempUser[1] not in Contributers
                            and tempUser[1] != "pre-commit-ci[bot]"
                        ):
                            Contributers.append(tempUser[1])

        # get the short commit id
        commit = repo.git.rev_parse(repo.head, short=True)

    result = [commit, branch, Contributers]
    return result