

def readAuthConfig(configFile, profilename):
    """ Reads config data from file, returns dictionary """
    import configparser
    import sys
    import os.path

    authConfig={}
    configFile = os.path.expanduser(configFile)
    config = configparser.RawConfigParser()
    try:
        config.read(configFile)

        authConfig['user'] = config.get(profilename, 'user')
        authConfig['password'] = config.get(profilename, 'password')
        authConfig['host'] = config.get(profilename, 'host')
        authConfig['database'] = config.get(profilename, 'database')
        return authConfig

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
