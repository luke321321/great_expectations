import pandas as pd
import numpy as np

from great_expectations.core.batch import Batch
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.core.expectation_validation_result import (
    ExpectationValidationResult,
)
from great_expectations.execution_engine import PandasExecutionEngine
from great_expectations.expectations.core.expect_column_mean_to_be_between import ExpectColumnMeanToBeBetween
from great_expectations.expectations.core.expect_column_stdev_to_be_between import ExpectColumnStdevToBeBetween


def test_expect_stdev_to_be_between_impl():
    df = pd.DataFrame({"a": [2, 17, 29]})
    expectationConfiguration = ExpectationConfiguration(
        expectation_type="expect_column_stdev_to_be_between",
        kwargs={"column": "a", "min_value":0, "max_value":4},
    )
    expectation = ExpectColumnStdevToBeBetween(expectationConfiguration)
    batch = Batch(data=df)
    result = expectation.validate(
        batches={"batch_id": batch}, execution_engine=PandasExecutionEngine()
    )
    assert result == ExpectationValidationResult(success=False,)