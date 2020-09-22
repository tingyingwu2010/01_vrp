import os
from shutil import copyfile
from datetime import datetime
import time
import configparser
import logging
from itertools import product
import random

import numpy as np # type: ignore
import pandas as pd # type: ignore
import tensorflow as tf # type: ignore

def set_seed(seed: int) -> None:
    try:
        if isinstance(seed, int):
            random.seed(seed)
            np.random.seed(seed)
            tf.random.set_seed(seed)
        else:
            raise ValueError(f'Expected an int to set seed, got: {seed} instead')
    except ValueError as err1:
        raise ValueError(err1)
    

# def current_timestamp(timestamp=time.localtime()):
#     ''' Formats the current time to use as a folder name '''
#     return time.strftime('%Y%m%d_%H%M%S', timestamp)


# def make_dirs(path):
#     ''' Makes a folder if it doesn't exist '''
#     if not os.path.exists(path):
#         os.makedirs(path)


# def read_config(path):
#     ''' Parses the config file '''
#     config = configparser.ConfigParser()
#     config.read(path)
    
#     return config


# def copy_config(source, destination_folder):

#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)

#     destination_path = os.path.join(destination_folder, "config.properties")

#     if os.path.exists(source):
#         copyfile(source, destination_path)
#         print(f'Successfully copied "config.properties" file to "{destination_path}"')


# def calculate_distance(origin, destination, method='euclidean'):
#     ''' Calculate distance between an origin and destination pair. '''
#     # TODO: Calculate reward function that loops through entire state.
#     # Use NEGATIVE Euclidean distance (so that we want to maximise this).

#     if method == 'euclidean':
#         distance = np.linalg.norm(destination[:2] - origin[:2])
#     return -1 * distance


# def generate_runs_folder(flag_save, folder_description, flag_prod,
#                          path_save_runs, path_config, path_train,
#                          path_env, path_policy):

#     # Save a log, config file, and this script for all runs
#     save_folder = current_timestamp(timestamp=time.localtime())

#     parameters = folder_description.split('-')
#     parameters.insert(0, save_folder)
#     folder_path = ('-').join(parameters)
#     if flag_prod is True:
#         folder_path_full = os.path.join(path_save_runs, 'PROD-' + folder_path)
#     elif flag_prod is False:
#         folder_path_full = os.path.join(path_save_runs, 'DEV-' + folder_path)

#     if (not os.path.exists(folder_path_full)) and (flag_save is True):
#         os.makedirs(folder_path_full)
#         print(f'Successfully generated runs folder at:\n"{folder_path_full}"\n')
        
#         copy_config(source=path_config,
#                     destination_folder=folder_path_full)
        
#         copy_scripts(path_train=path_train,
#                      path_env=path_env,
#                      path_policy=path_policy,
#                      folder_path_full=folder_path_full)
        
#     elif flag_save is False:
#         print('WARNING: Currently not saving any configs, logs or scripts')
#     else:
#         raise ValueError(f"Was unable to make the path {folder_path_full}")
#     return folder_path_full


# def copy_scripts(path_train, path_env, path_policy, folder_path_full):

#     if not os.path.exists(folder_path_full):
#         os.makedirs(folder_path_full)

#     for script in [path_train, path_env, path_policy]:
#         if os.path.exists(script):
#             script_name = os.path.basename(script)
#             destination = os.path.join(folder_path_full, script_name)
#             copyfile(script, destination)
#             print(f'Successfully copied "{script_name}" to "{destination}"')
#         elif not os.path.exists(script):
#             raise ValueError(f"Could not find file {script}")
            
            
# def save_logs(folder_path_full, flag_save=False,
#               flag_print_logs=True, 
#               path_temp_log='.', 
#               log_level=logging.DEBUG,
#               log_name='log.log',
#               config=None):
#     '''Good example at https://realpython.com/python-logging/#the-logging-module'''
#     log_path = os.path.join(folder_path_full, log_name)

#     logger = logging.getLogger(__name__)
#     logger.setLevel(log_level)

#     formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%H:%M:%S')

#     if flag_save is True:
#         file_handler = logging.FileHandler(log_path)
#         file_handler.setLevel(log_level)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)

#     if flag_print_logs is True:
#         temp_file_handler = logging.FileHandler(path_temp_log, 'w')
#         temp_file_handler.setLevel(log_level)
#         temp_file_handler.setFormatter(formatter)
#         logger.addHandler(temp_file_handler)

#     for section in config.sections():
#         logger.debug(f'{section} has key value pairs:')
#         for key, value in config.items(section):
#             # :20 pads the keys so that the values are aligned vertically
#             logger.info(f'\t{key:20}{value}')
#         logger.info('') # Formatting

#     return logger


# def get_hyperparams(hyperparams):
    
#     hyperparam_dict = dict()
    
#     for hyperparam in hyperparams:
#         hyperparam = hyperparam.split(', ')
        
#         assert hyperparam[0].isnumeric() is False, f'First string in list should be a name, not a number, got: {hyperparam[0]}'
            
#         name = hyperparam[0] # Expecting something like 'ALPHAS'
    
#         if hyperparam[1].strip().isalpha() is False:
#             try:
#                 hyperparam_dict[name] = [float(x.strip()) for x in hyperparam[1: ]]
#             except:
#                 print(f'Trying to convert hyperparams to float, but not working. Likely need to check if each element is a float: {hyperparam[1: ]}')
#         elif hyperparam[1].strip().isalpha() is True:
#             try:
#                 hyperparam_dict[name] = [True if x.strip() == 'True' else False if x.strip() == 'False' else 'Error' for x in hyperparam[1: ]]
#             except:
#                 print(f'Trying to convert hyperparameters to boolean, but not working, got {hyperparam[1: ]}')
    
#     return hyperparam_dict


# def init_experimental_design(hyperparams, additional_columns, path_hyperparams,
#                              flag_save, agent_seed, env_seed,
#                              n_repetitions):
    
#     # A few constants that are needed for finding combinations
#     columns = [str(x) for x in hyperparams]
#     n_hyperparams = len(columns)
#     hyperparam_values = [hyperparams[columns[i]] for i in range(len(columns))]
    
#     # Maybe want some additional columns, like a progress column
#     additional_columns = additional_columns.split(', ')
#     for column in additional_columns:
#         columns.append(column)
    
#     # A bit crap it has to be hard coded to an arbitrarily large number. However
#     # Hardcoding is seen to be preferable to adding more complex code which litters.
#     experimental_design = pd.DataFrame(index=range(2000), columns=columns)
    
#     # Find all combinations of hyperparameters (i.e. grid search).
#     combination = 0 # Tracks index of combination currently working on
#     for i, val in enumerate(product(*hyperparam_values)):
#         for j in range(n_repetitions):
#             for k in range(n_hyperparams):
#                 experimental_design.iat[combination, k] = val[k]
#             experimental_design.loc[combination, 'AgentSeed'] = agent_seed[j] # This is a list of ints
#             experimental_design.loc[combination, 'EnvSeed'] = env_seed # This is an int
#             experimental_design.loc[combination, 'Repetition'] = j
#             experimental_design.loc[combination, 'Experiment'] = i
#             combination += 1

#     if flag_save is True:        
#         experimental_design.to_csv(f'{path_hyperparams}', index_label='Index')
#         print(f'Successfully saved the Experimental Design to {path_hyperparams}')
#     else:
#         print(f'WARNING: Did not save Experimental Design.')
        
#     return experimental_design


# def write_start_experimental_design(experimental_design, combination, n_experiments, path_hyperparams, flag_save):
    
#     experiment_start = datetime.now()
#     if combination >= 0:
#         experimental_design.loc[combination, 'Progress'] = 'In Progress'
#         experimental_design.loc[combination, 'Start'] = experiment_start
        
#     if combination >= 1:
#         experimental_design.loc[combination - 1, 'Progress'] = 'Finished'
    
#     if flag_save is True:
#         experimental_design.to_csv(path_hyperparams, index_label='Index')


# def write_finish_experimental_design(experimental_design, combination, n_experiments, path_hyperparams, flag_save, logger):
    
#     experiment_finish = datetime.now()
    
#     experimental_design.loc[combination, 'Progress'] = 'Finished'
#     experimental_design.loc[combination, 'Finish'] = experiment_finish
    
#     experiment_start = experimental_design.loc[combination, 'Start']
#     elapsed = (experiment_finish - experiment_start).total_seconds()
#     experimental_design.loc[combination, 'Elapsed (s)'] = round(elapsed, 2)
    
#     logger.info(f'This experiment took {elapsed} seconds to run')
    
#     if flag_save is True:
#         experimental_design.to_csv(path_hyperparams, index_label='Index')
        
        
# def copy_files(source, destination):
#     dirname = os.path.dirname(destination)
#     if not os.path.exists(dirname):
#         os.makedirs(dirname)
        
#     copyfile(source, destination)
#     print(f'Successfully copied from "{source}" to "{destination}"')
