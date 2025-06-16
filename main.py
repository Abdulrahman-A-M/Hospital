from operations_manager import OperationsManager
from utility import *


if __name__ == '__main__':
    main = OperationsManager()
    generating_random_data(main)
    main.run()