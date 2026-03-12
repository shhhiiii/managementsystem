def bubble_sort(records, index):
    '''
    This function sorts a list of records using the Bubble Sort algorithm.
    
    I use this instead of Python's built-in sort to show that I understand how sorting algorithms work.
    The sorting is done based on a specific column (index) in each record, for example, name or subject.
    '''
    n = len(records)
    for i in range(n):
        # In each iteration, I compare adjacent items and move the larger one to the right.
        for j in range(0, n - i - 1):
            # I convert both values to lowercase strings
            if str(records[j][index]).lower() > str(records[j + 1][index]).lower():
                # If current value is greater than next one, I swap them.
                records[j], records[j + 1] = records[j + 1], records[j]
    # After all passes, the list is sorted in ascending order by the selected column.
    return records


def linear_search(records, index, target):
    '''
    This function searches for records that exactly match a target value in a specific column.
    
    Instead of using SQL WHERE clauses, I manually search through each row.
    This demonstrates how linear search works, useful for understanding algorithmic thinking.
    '''
    result = []
    target = str(target).lower()  # Convert target to lowercase to ensure case-insensitive match

    for row in records:
        '''
        For each record, I check the value in the selected column (index).
        If it matches the target (also in lowercase), I add it to the result list.
        '''
        if str(row[index]).lower() == target:
            result.append(row)

    # After the loop, I return all rows where the value matches exactly.
    return result
