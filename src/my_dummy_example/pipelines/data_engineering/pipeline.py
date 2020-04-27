from kedro.pipeline import node, Pipeline
from my_dummy_example.pipelines.data_engineering.first_node import (
    preprocess_dummy_data
)

from my_dummy_example.pipelines.data_engineering.second_node import (
    preprocess_again_dummy_data
)   

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_dummy_data,
                inputs="mydummydata",
                outputs="preprocess_dummy_data_mydummydata_output",
                name="first_node_registered_name",
            ),
            # the order does not matter
            # the order is determined based on the input and output
            node(
                func=preprocess_again_dummy_data,
                inputs="preprocess_dummy_data_mydummydata_output",
                outputs="preprocessed_data",
                name="second_node_registered_name",
            ),
        ]
    )
