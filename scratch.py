def inc(alist):
  if len(alist) == 2:
    return alist[0] <= alist[1]
  if alist[0] > alist[1]:
    return False
  return inc(alist[1:])
print(inc([1, 2, 5, 4, 8]))