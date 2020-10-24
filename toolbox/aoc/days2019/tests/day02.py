from toolbox.aoc.days2019 import day02

def test_check_computer():
    assert day02.Computer([1,9,10,3,2,3,11,0,99,30,40,50]).run() == [3500,9,10,70,2,3,11,0,99,30,40,50]
    assert day02.Computer([1,1,1,4,99,5,6,0,99]).run() == [30,1,1,4,2,5,6,0,99]
    return
