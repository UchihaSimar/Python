# Argument Passing & Reassignment vs. In-Place Mutation
def process_data(lst, val):
    lst.append(val)   # In-place mutation: updates caller's list
    lst = [100, 200]  # Local name re-binding: caller remains unaffected

data = [1, 2]
process_data(data, 3)
print(data)
# data is now [1, 2, 3]


# Shallow vs. Deep Copying (copy module)
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999
print(original)
print(shallow)
print(deep)

# shallow[0][0] -> 999 (Shared reference to nested list)
# deep[0][0]    -> 1   (Fully isolated clone)