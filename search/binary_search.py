from search.search import Search

class BinarySearch(Search):
    def search(self, list, item):
        left = 0
        right = len(list) - 1
        while left<=right:
            mid = int((left+right)/2)

            if list[mid] == item:
                return mid
            elif list[mid] < item:
                left = mid
            else:
                right = mid
        
        return None

