class RelationException(Exception):
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def __str__(self):
        return ("Are you sure that {} and {} "\
        "are in love with each other?".format(self.p1,self.p2))
        
relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    try:
        if relation[pa] != pb:
            raise RelationException(pa,pb)
    except KeyError:
        print("No relation found")
        raise RelationException(pa,pb)
        # TODO: raise exception
        # TIPS: 這個地方會需要 raise 兩種 exception
        
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)