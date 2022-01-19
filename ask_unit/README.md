    test_case = [
        [38850, 39800, 40250, 38670],
        [0.763, 0.77, 0.785, 0.747],
        [3735, 3735, 3735, 3735],
        [3010, 3010, 3010, 3010],
        [116.2, 116.8, 117, 116.2],
        [3369, 3495, 3495, 3369],
        [3450, 3450, 3450, 3450],
        [35.2, 35.2, 35.2, 35.2],
        [36.88, 36.88, 36.88, 36.87],
        [708.4, 727, 727, 700.1],
        [578, 571, 588, 565]

    ]

--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[38850, 39800, 40250, 38670] -> [50, 100, 50, 10] -> 10

close price -> close fixed unit  
38670 -> 10

max(min recent unit, close fixed unit) -> result unit  
max(10, 10) -> 10
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[0.763, 0.77, 0.785, 0.747] -> [0.001, 0.01, 0.001, 0.001] -> 0.001

close price -> close fixed unit  
0.747 -> 0.0001  

max(min recent unit, close fixed unit) -> result unit  
max(0.001, 0.0001) -> 0.001
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[3735, 3735, 3735, 3735] -> [5, 5, 5, 5] -> 5

close price -> close fixed unit  
3735 -> 1

max(min recent unit, close fixed unit) -> result unit    
max(5, 1) -> 5
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[3010, 3010, 3010, 3010] -> [10, 10, 10, 10] -> 10

close price -> close fixed unit  
3010 -> 1

max(min recent unit, close fixed unit) -> result unit  
max(10, 1) -> 10
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[116.2, 116.8, 117, 116.2] -> [0.1, 0.1, 1, 0.1] -> 0.1

close price -> close fixed unit  
116.2 -> 0.1

max(min recent unit, close fixed unit) -> result unit  
max(0.1, 0.1) -> 0.1
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[3369, 3495, 3495, 3369] -> [1, 5, 5, 1] -> 1

close price -> close fixed unit  
3369 -> 1

max(min recent unit, close fixed unit) -> result unit  
max(1, 1) -> 1
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[3450, 3450, 3450, 3450] -> [50, 50, 50, 50] -> 50

close price -> close fixed unit  
3450 -> 1

max(min recent unit, close fixed unit) -> result unit  
max(50, 1) -> 50
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[35.2, 35.2, 35.2, 35.2] -> [0.1, 0.1, 0.1, 0.1] -> 0.1

close price -> close fixed unit  
35.2 -> 0.01

max(min recent unit, close fixed unit) -> result unit  
max(0.1, 0.01) -> 0.1
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[36.88, 36.88, 36.88, 36.87] -> [0.01, 0.01, 0.01, 0.01] -> 0.01

close price -> close fixed unit  
36.87 -> 0.01

max(min recent unit, close fixed unit) -> result unit  
max(0.01, 0.01) -> 0.01
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[708.4, 727, 727, 700.1] -> [0.1, 1, 1, 0.1] -> 0.1

close price -> close fixed unit  
700.1 -> 0.1

max(min recent unit, close fixed unit) -> result unit  
max(0.1, 0.1) -> 0.1
--------------------------------------------------
recent price -> recent unit -> min(recent_unit)  
[578, 571, 588, 565] -> [1, 1, 1, 5] -> 1

close price -> close fixed unit  
565 -> 0.1

max(min recent unit, close fixed unit) -> result unit  
max(1, 0.1) -> 1
--------------------------------------------------