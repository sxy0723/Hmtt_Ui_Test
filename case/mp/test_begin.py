import pytest

from utils import DriverUtils


@pytest.mark.run(order=1)
class TestBegin:
    def test_begin(self):
        # 关闭关闭浏览器驱动的开关
        DriverUtils.charge_mp_key(False)
