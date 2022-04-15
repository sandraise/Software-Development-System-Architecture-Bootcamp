# for i,j in enumerate([1,4,7,3,7,2,53]):
#     print(i,j)

def location_finder(loc,target):
        for i,j in enumerate(loc):
            if j == target:
                return("Found at position: ")
        return("Oops, not found!")


def food_finder(snack,target):
        for i,j in enumerate(snack):
            if j == target:
                return("Found at position: ")
        return("Oops, not found!")