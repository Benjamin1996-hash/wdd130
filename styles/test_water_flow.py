from pytest import approx
import pytest
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pytest.approx(pressure_gain_from_water_height(0.0), abs=0.001) == 0.000
    assert pytest.approx(pressure_gain_from_water_height(30.2), abs=0.001) == 295.628
    assert pytest.approx(pressure_gain_from_water_height(50.0), abs=0.001) == 489.450

def test_pressure_loss_from_pipe():
    assert pytest.approx(pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75), abs=0.001) == -113.008
    assert pytest.approx(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65), abs=0.001) == -100.462
    assert pytest.approx(pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65), abs=0.001) == -61.576
    assert pytest.approx(pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65), abs=0.001) == -110.884

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
