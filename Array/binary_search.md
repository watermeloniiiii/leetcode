# 704. Binary Search
<span style=font-size:20px;font-weight:700> Problem description </span>  
<span style=font-size:15px>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  
You must write an algorithm with ```O(log n)``` runtime complexity.</span>
<br></br>

### ***Solution***:
<span style=font-size:15px>There are basically three possible scanerios:</span>  
1. the target value is larger than the rightmost value, then direct return ```len(nums)```  
2. the target value is smaller than the leftmost value, then direct return ```0``` 
3. the target value is in the between and this scanerio is more complex, there are two ending conditions:
    - when ```left=right``` and both ```nums[left]``` and ```nums[right]``` are larger than the target, as ```nums[middle] > target```, this will invoke the statement ```right = middle - 1``` and the ```while``` loop will stop. The correct postion should be between ```right=middle-1=left-1``` and ```left```, which is ```left``` or ```right + 1``` or ```middle```
    - when ```left=right``` and both ```nums[left]``` and ```nums[right]``` are smaller than the target, as ```nums[middle] < target```, this will invoke the statement ```left = middle + 1``` and the ```while``` loop will stop. The correct postion should be between ```right=middle=left-1``` and ```left```, which is ```left``` or ```right + 1``` or ```middle + 1```
    - combining the two cases, the answer should be either ```left``` or ```right + 1```
<br></br>
### ***Question***
1. <span style=color:red>**Is the ending condition always the same?**</span>
    - Yes. No matter what scenario it is, the ```left``` element will eventually become equal to the ```right``` element and then either the ```left``` or the ```right``` element will change depends on whehter their value is larger or smaller than the target
    - Example 1:
    ```python 
        nums, target = [1,3], 2
        # step 1
        left, right, middle = 0, 0, 0
        nums[middle] = 1 < target = 2 
        right = middle - 1 = -1 < left
        # step 2
        break the loop as left > right
    ``` 
    - Example 2:
    ```python 
        nums = [1,3,4]
        target = 2
        # step 1
        left, middle, right  = 0, 1, 2
        nums[middle] = 3 > target = 2 
        right = middle - 1 = 0
        # step 2
        left, middle, right = 0, 0, 0
        nums[middle] = 1 < target = 2
        left = middle + 1 = 1 > right
        # step 3
        break the loop as left > right
    ```
    - Example 3
    ```python 
        nums = [1,2,4,5]
        target = 3
        # step 1
        left, middle, right  = 0, 1, 3
        nums[middle] = 2 < target = 3 
        left = middle + 1 = 2
        # step 2
        left, middle, right = 2, 2, 3
        nums[middle] = 4 > target = 3
        right = middle - 1 = 1 < left
        # step 3
        break the loop as left > right
    ```
2. <span style=color:red>**Why it will always find the target when it exists?**</span>

<br></br>
## 1351. Count Negative Numbers in a Sorted Matrix
<span style=font-size:20px;font-weight:700> Problem description </span> 

<span style=font-size:15px>Given a ```m x n``` matrix ```grid``` which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in ```grid```</span>.

### ***Solution***  
1. We can loop through each row first, this step give you a time complexity of ```n```, where ```n``` is the number of rows
```python
for i in range(len(grid))
```
2. then for each row ```grid[i]```, it is a non-increasing list that we can apply the classical binary search algorithm. Note that there will be <span style=color:red>**three**</span> scenarios:
- all elements are negative, which means ```grid[i][0] < 0```. In this scenario, the total count should be added with ```len(grid[i]```
```python
 if grid[i][0] < 0:
    count += len(grid[i])
    continue
```
- all elements are larger than or equal to 0, which means ```grid[i][-1] >= 0```. In this scenario, the total count should be added with ```0```
```python
 elif grid[i][-1] >= 0:
    count += 0
    continue
```
- parts of the elements are negative, the problem turns to **find the correct position to insert an element**. In this scenario, no ```0``` can be found and eventually ```left``` will  larger than ```right```  

  - when ```left = right``` and both ```grid[i][left] < 0``` and ```grid[i][right] < 0```, as the condition ```grid[i][middle] < 0``` is invoked, ```right``` will become ```middle - 1```. In this situation, starting from ```left = middle = right + 1```, all elements are negative
  - when ```left = right``` and both ```grid[i][left] > 0``` and ```grid[i][right] > 0```, as the condition ```grid[i][middle] > 0``` is invoked, ```left``` will become ```middle + 1```. In this situation, starting from ```left = middle + 1 = right + 1```, all elements are negative
- combining the two, the position should either be ```left``` or ```right + 1```
```python
left = 0
right = len(grid[i]) - 1
while left <= right:
    middle = (left + right) // 2
    # when 0 is found in the array, e.g., [3,2,0,-1], 0 is at location 2, and negative count should be len([3,2,0,-1])- middle - 1 
    if grid[i][middle] == 0:
        count += len(grid[i]) - middle - 1
    elif grid[i][middle] > 0:
        left = middle + 1
    else:
        right = middle - 1

```
- 
 
