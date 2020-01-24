import sklearn
from sklearn.model_selection import train_test_split


class data_split:

    def __init__(self, df):
        self.df = df
        self.split_data()

    def split_data(self):
        '''
        function to split data into train, test, validate data
        The dataframe is split into 15% test, then 85% train. 
        The train data set is then further split into 20% validation
        and 80% train dataset. 
        So the final result is 15% of original data = test
        about 15% of original data is validation,
        and 70% of original data is train. 
        '''

        self.train, self.test = train_test_split(
            self.df, test_size=0.15, random_state=42)

        self.train, self.val = train_test_split(
            self.train, test_size=0.20, random_state=42)

        return self.train, self.test, self.val

    # function to split into target and features dataset.

    def get_target(self, target_feature):
        '''
        function to split into target and features dataset.
        Target = target from the dataframe. 
        '''

        self.target = target_feature
        self.features = self.train.columns.drop(self.target)

        self.x_train = self.train[self.features]
        self.y_train = self.train[self.target]
        self.x_val = self.val[self.features]
        self.y_val = self.val[self.target]
        self.x_test = self.test[self.features]
        self.y_test = self.test[self.target]

        return self.x_train, self.y_train, self.x_val, self.y_val, self.x_test, self.y_test
