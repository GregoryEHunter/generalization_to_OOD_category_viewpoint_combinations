import pickle
import os
from loader.multi_attribute_loader_file_list import FileListFolder as multi_attribute_loader_file_list
from loader.multi_attribute_loader_file_list_ilab import FileListFolder as multi_attribute_loader_file_list_ilab
import sys

print(__file__)
loader_folder = '/'.join(__file__.split('/')[:-1])
print(loader_folder)
with open('%s/category_to_class_number_per_car_synthetic_only_cars_no_police.p'%loader_folder,'rb') as F:
    category_to_class_number_per_car_synthetic_only_cars_no_police = pickle.load(F)

with open('%s/category_to_class_number_ilab_5_cars.p'%loader_folder,'rb') as F:
    category_to_class_number_ilab_5_cars = pickle.load(F)

def get_loader(name):
    """get_loader
    :param name:
    """
    return {
        "multi_attribute_loader_file_list" : multi_attribute_loader_file_list,
        "multi_attribute_loader_file_list_ilab" : multi_attribute_loader_file_list_ilab,
    }[name]



def get_loader_classes(name):
    """get_loader_classes
    :param name:
    """
    return {
        "multi_attribute_loader_file_list":category_to_class_number_per_car_synthetic_only_cars_no_police,
        "multi_attribute_loader_file_list_ilab":category_to_class_number_ilab_5_cars,
    }[name]
