import yaml

# Note to self - assumed that the yaml files configure logging
# so the print statements currently ok here
def load_yaml(filename):
    print 'Looking for file here:"{0}"'.format(filename)
    try:
        with open(filename, 'r') as config_file:
            return yaml.load(config_file)
    except IOError:
        msg = 'Unable to find config file {file}'.format(file=filename)
        print msg
        print 'The program will now exit'
        raise SystemExit
