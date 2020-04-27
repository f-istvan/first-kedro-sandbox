from kedro.pipeline import node, Pipeline
from my_dummy_example.pipelines.data_engineering.first_node import (
    preprocess_dummy_data
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_dummy_data,
                inputs="mydummydata",
                outputs="preprocessed_companies",
                name="first_node_registered_name",
            ),
        ]
    )
