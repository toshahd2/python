def search_data(text, data):
    if len(data) > 0:
        mylist = []
        for item in data:
            if text in item:
                mylist.append(item)
        if mylist == []:
            return None
        else:
            return mylist
    else:
        return None