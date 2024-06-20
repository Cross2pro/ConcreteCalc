import configparser

def read_key_from_config(config_file, section, key):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config[section][key]

def write_key_to_config(config_file, section, key, value):
    config = configparser.ConfigParser()
    config.read(config_file)
    config[section][key] = value
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def write_int_toConfig(key,value):

    write_key_to_config('config.ini','config',key,value)

def read_int_fromConfig(key):

    return int(read_key_from_config('config.ini','config',key) )