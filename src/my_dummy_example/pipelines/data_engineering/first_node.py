import pandas as pd

def preprocess_dummy_data(dummy_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for dummy_data.

        Args:
            dummy_data: Source data.
        Returns:
            Preprocessed data.

    """

    print('-- preprocess_dummy_data --')
    print(dummy_data)
    

    mod_dummy_data = dummy_data.append({'product_id' : '88888888' , 'amount' : 99} , ignore_index=True)
    print(mod_dummy_data)

    return mod_dummy_data