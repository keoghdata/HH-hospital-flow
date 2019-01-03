from flosp.data import Data

class Interface:
    """
    class which contains all actions (methods) available to user.
    """
    def __init__(self):
        print('created_flosp')
        self.data = Data()
        pass
    
    def load_data(self):
        pass

    def run_checks(self):
        """An output of current status of flosp analysis, including:
        - Prints current status of data 
        - Gives summary of errors
        """
        pass

    def make_new_tables(self):
        """Create all aggregate tables possible i.e. houlry and daily tables """
        pass

    def extract_data(self):
        """ extract dataframe for user manipulation """
        pass

    def plot(self):
        """ Plot all graphs and tables possible with current analysis """ 
        pass

