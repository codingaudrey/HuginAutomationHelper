import sys
from ConnectionHandlerDropbox import ConnectionHandlerDropbox


if __name__ == '__main__':
    credentials = sys.argv[0]
    dbx = ConnectionHandlerDropbox(credentials)
    print(dbx.create_folders())
