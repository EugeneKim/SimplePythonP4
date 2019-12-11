# This python source is a very simple example which shows how to use p4python module.

from P4 import P4, P4Exception

def GetFileContent(p4: P4, file: str) -> str:
    try:
        content = p4.run('print', file)
        return True, content
    except P4Exception as ex:
        if ex.errors:
            raise ex
        elif ex.warnings and isinstance(ex.warnings, list):
            if any([s for s in ex.warnings if '- no such file(s)' in s]):
                return False, None
            else:
                raise ex

def P4SimpleUsage():
    p4 = P4()

    p4.port = 'p4server:1666'
    p4.user = 'joe'
    p4.password = 'joe_password'

    # Establish a new session to the server.
    p4.connect()

    if not p4.connected():
        print ("Not connected!")
        pass

    # run "p4 info" command.
    info = p4.run("info")

    for i in info:
        for k, v in i.items():
            print("{}: {}".format(k, v))

    # run "p4 login" command.
    p4.run_login()

    # run "p4 print" to get content of a file in the repository without syncing.
    file = '//Projects/Python/Info.txt'
    exists, content = GetFileContent(p4, file)

    if exists:
        print(content)
    else:
        print("file not found: {}".format)
   
    # run "p4 logout" command.
    p4.run("logout")

    # Disconect current session.
    p4.disconnect()

P4SimpleUsage()
