def kairosAuthConfig(configFile, profilename):
    """ Reads config data from file, returns dictionary """
    import configparser
    import sys
    import os.path

    authConfig={}
    configFile = os.path.expanduser(configFile)
    config = configparser.RawConfigParser()
    try:
        config.read(configFile)

        authConfig['app_id'] = config.get(profilename, 'app_id')
        authConfig['app_key'] = config.get(profilename, 'app_key')
        return authConfig

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


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

def getArgs(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description="Hack stuff.")
    parser.add_argument('--credentials', '-C', default="credentials.ini", help='Location of credential file')
    parser.add_argument('--profile', '-P', default="default", help='Profile to use')
    options = parser.parse_args()

    return parser.parse_args(argv)
