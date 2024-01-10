class Search:
    def search(self, list, item):
        for i in range(len(list)):
            if list[i] == item:
                return i
        return None

