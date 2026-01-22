import pytest
from main import OpenFile, filter_num, text_generator
from contextlib import nullcontext as not_raise

class TestOpenFile:
    @pytest.mark.anomaly_check
    @pytest.mark.parametrize(
        "num, res",
        [
            pytest.param(90, True, id='wrong'),
            pytest.param(70, False, id='correct'),
            pytest.param(99, True, id='wrong'),
            pytest.param(89, True, id='wrong'),
            pytest.param(6, False, id='correct'),
            pytest.param(91, True, id='wrong'),
            pytest.param(10, False, id='correct'),
            pytest.param(81, True, id='wrong'),
            pytest.param(9, False, id='correct'),
            pytest.param(95, True, id='wrong'),
            pytest.param(98, True, id='wrong'),
            pytest.param(50, False, id='correct'),
            pytest.param(100, True, id='wrong'),
            pytest.param(90, True, id='wrong'),
        ]
    )
    def test_anomaly(self, num, res):
        assert filter_num(num) == res


