import itertools

class Node:

    id_iter = itertools.count()

    def __init__(self, question, answer):
        self.answer = answer
        self.nodes = []
        self.data = question
        self.id = next(self.id_iter)

    def __str__(self):
        return self.answer

    def __int__(self):
        return len(self.nodes)
            

#Makes the tree and then returns the root node.
#This is the worst code I have ever written. I'm having an amazing time, unironically
def build_tree():

    root = Node("What was your favorite subject in high school?", "root")

    nextq = "How do you derive meaning in your life?"
    root.nodes.append(Node(nextq,"Math"))
    root.nodes.append(Node(nextq,"Science"))
    root.nodes.append(Node(nextq,"English"))
    root.nodes.append(Node(nextq,"History"))
    root.nodes.append(Node(nextq,"Music/Art"))

    #For each node attached to the root node, create the following progression
    for i in range(0,int(root)-1):
        nextq = "Do you prefer to work with others or by yourself?"
        root.nodes[i].nodes.append(Node(nextq, "Through Work"))
        root.nodes[i].nodes.append(Node(nextq, "Through Family and Friends"))

        #Next Question for the "Through Work" answer.
        nextq_work = "Would you like to work in education?"

        #Next Question for the "Through Family and Friends" answer.
        nextq_family = "Would you rather be wealthy or respected by your peers?"
        root.nodes[i].nodes[0].nodes.append(Node(nextq_work, "By Myself"))
        root.nodes[i].nodes[0].nodes.append(Node(nextq_work, "With Others"))

        root.nodes[i].nodes[1].nodes.append(Node(nextq_family, "By Myself"))
        root.nodes[i].nodes[1].nodes.append(Node(nextq_family, "With Others"))


        #Terminating tree
        root.nodes[i].nodes[0].nodes[0].nodes.append(Node("Bachelor of Science in Mathematics, Bachelor of Science in Secondary Education, Bachelor of Science in Middle Grades Education", "Yes"))
        root.nodes[i].nodes[0].nodes[0].nodes.append(Node("Bachelor of Science in Mathematics, Bachelor of Science in Physics, Bachelor of Science in Mechanical Engineering", "No"))

        #We messed this one up and beyond!!! Dont forget to re-check!!
        root.nodes[i].nodes[0].nodes[1].nodes.append(Node("Bachelor of Science in Computer Engineering, Bachelor of Business Administration in Accounting, Bachelor of Business Administration in Finance", "Wealthy"))
        root.nodes[i].nodes[0].nodes[1].nodes.append(Node("Bachelor of Science in Civil Engineering, Bachelor of Business Administration in Economics, Bachelor of Science in Industrial and Systems Engineering", "Respected"))

        root.nodes[i].nodes[1].nodes[0].nodes.append(Node("", "Respected"))
        root.nodes[i].nodes[1].nodes[0].nodes.append(Node("", "Respected"))
         
        #          i        1        1
        #          i        1        1

    