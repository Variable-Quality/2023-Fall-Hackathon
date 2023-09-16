"""
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
"""

    
# Prototyping
#
q1 = "What was your favorite subject in high school? (Math, Science, Literature, History, Art)"
q2 = "How do you derive meaning in your life? (Through work, Family and friends)"
q3 = "Do you prefer to work with people or by yourself? (With people, Solo)"
q4_1 = "Would you like to work in education? (Yes, No)"
q4_2 = "Would you rather be wealthy or respected by your peers? (Wealthy, Respected)"
q5_1 = "Which age group? (Elementary, Middle, High, College)"
q5_2 = "Do you like computers? (Yes, No)"
q5_3 = "Would you like to explore cultures or people in general? (Cultures, General)"

level = 1
ext_flag = False
edu_flag = False
math_flag = False
lit_flag = False
lit_woke_flag = False


class TreeNode:
    def __init__(self, question):
        self.question = question
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    print(" " * level + str(node.question))
    for child in node.children:
        print_tree(child, level + 1)

def conditional_traversal(node):
    user_input = input(node.question)
    # Requires Python > 3.10
    match level:
        case 1: 
            match user_input: 
                case "math":
                    math_flag = True
                case "science":

                case "literature":

                case "history":

                case "art":

                case _ :
                    print("Unable to read user input")
        case 2: 
            match user_input: 
                case "through work":

                case "family and friends":

                case _:
                    print("Unable to read user input")

        case 3: 
            match user_input:
                case "with people":
                    ext_flag = True
                case "solo":

                case _:
                    print("Unable to read user input")
        case 4: 
            if ext_flag: # Education
                match user_input:
                    case "yes":
                        edu_flag = True
                    case "no":

                    case _:
                        print("Unable to read user input")
            else:
                match user_input: # Respect or money
                    case "wealthy":

                    case "respected":

                    case _:
                        print("Unable to read user input")
        case 5:
            if edu_flag: # age group
                match user_input:
                    case "Elementary":

                    case "Middle":

                    case "High":

                    case "College":

                    case _:
                        print("Unable to read user input")
            elif !edu_flag and math_flag: # Introverted math person interested in computers? 
                match user_input:
                    case "yes":

                    case "no":

                    case _:
                        print("Unable to read user input")
        case 6:
            match user_input: # In lit's longest path
                case "wealthy":

                case "respected":

                case _:
                    print("Unable to read user input")
        case 7:
            match user_input: # Still in lit's longest path
                case "cultures":

                case "general":

                case _:
                    print("Unable to read user input")
        case _:
            print("Some unknown error has occurred. Try again")

# Define Tree
#
# I could make this much less verbose but for readibility sake, I'll leave the
# variable instantiations
#
# First Level
root = TreeNode(q1)

# Second Level
math = TreeNode(q2)
sci = TreeNode(q2)
lit = TreeNode(q2)
hist = TreeNode(q2)
art = TreeNode(q2)

root.add_child(math)
root.add_child(sci)
root.add_child(lit)
root.add_child(hist)
root.add_child(art)

# Third Level
math_work = TreeNode(q3)
sci_work = TreeNode(q3)
lit_work = TreeNode(q3)
hist_work = TreeNode(q3)
art_work = TreeNode(q3)

math_fam = TreeNode(q3)
sci_fam = TreeNode(q3)
lit_fam = TreeNode(q3)
hist_fam = TreeNode(q3)
art_fam = TreeNode(q3)

math.add_child(math_work)
math.add_child(math_fam)
sci.add_child(sci_work)
sci.add_child(sci_fam)
lit.add_child(lit_work)
lit.add_child(lit_fam)
hist.add_child(hist_work)
hist.add_child(hist_fam)
art.add_child(art_work)
art.add_child(art_fam)

# Fourth Level
math_work_ext = TreeNode(q4_1)
sci_work_ext = TreeNode(q4_1)
lit_work_ext = TreeNode(q4_1)
hist_work_ext = TreeNode(q4_1)
art_work_ext = TreeNode(q4_1)

math_work_int = TreeNode(q4_2)
sci_work_int = TreeNode(q4_2)
lit_work_int = TreeNode(q4_2)
hist_work_int = TreeNode(q4_2)
art_work_int = TreeNode(q4_2)

math_fam_ext = TreeNode(q4_1)
sci_fam_ext = TreeNode(q4_1)
lit_fam_ext = TreeNode(q4_1)
hist_fam_ext = TreeNode(q4_1)
art_fam_ext = TreeNode(q4_1)

math_fam_int = TreeNode(q4_2)
sci_fam_int = TreeNode(q4_2)
lit_fam_int = TreeNode(q4_2)
hist_fam_int = TreeNode(q4_2)
art_fam_int = TreeNode(q4_2)

math_work.add_child(math_work_ext)
math_work.add_child(math_work_int)
math_fam.add_child(math_fam_ext)
math_fam.add_child(math_fam_int)

sci_work.add_child(sci_work_ext)
sci_work.add_child(sci_work_int)
sci_fam.add_child(sci_fam_ext)
sci_fam.add_child(sci_fam_int)

lit_work.add_child(lit_work_ext)
lit_work.add_child(lit_work_int)
lit_fam.add_child(lit_fam_ext)
lit_fam.add_child(lit_fam_int)

hist_work.add_child(hist_work_ext)
hist_work.add_child(hist_work_ext)
hist_fam.add_child(hist_fam_int)
hist_fam.add_child(hist_fam_int)

art_work.add_child(art_work_ext)
art_work.add_child(art_work_ext)
art_fam.add_child(art_fam_int)
art_fam.add_child(art_fam_int)

# Fifth Level
math_work_ext_edu = TreeNode(q5_1)
sci_work_ext_edu = TreeNode(q5_1)
lit_work_ext_edu = TreeNode(q5_1)
hist_work_ext_edu = TreeNode(q5_1)
art_work_ext_edu = TreeNode(q5_1)

math_work_ext_noedu = TreeNode("Mathematics, Finance, Mechanical Engineering, or Computer Engineering")
sci_work_ext_noedu = TreeNode("Integrated Health Sciences, Biology, or Nursing")
lit_work_ext_noedu = TreeNode(q4_2)
hist_work_ext_noedu = TreeNode("International Affairs, Political Science, or Media and Entertainment")
art_work_ext_noedu = TreeNode("Media and Entertainment, Digital Animation, or Theatre and Performance Studies")

math_fam_ext_edu = TreeNode(q5_1)
sci_fam_ext_edu = TreeNode(q5_1)
lit_fam_ext_edu = TreeNode(q5_1)
hist_fam_ext_edu = TreeNode(q5_1)
art_fam_ext_edu = TreeNode(q5_1)

math_fam_ext_noedu = TreeNode("Electrical Engineering Technology")
sci_fam_ext_noedu = TreeNode("Public Health Education")
lit_fam_ext_noedu = TreeNode(q4_2)
hist_fam_ext_noedu = TreeNode("Human Services, or Theatre and Performance Studies")
art_fam_ext_noedu = TreeNode("Theatre and Performance Studies")

math_work_int_money = TreeNode(q5_2)
sci_work_int_money = TreeNode("Physics")
lit_work_int_money = TreeNode("Marketing, Hospitality, or Management")
hist_work_int_money = TreeNode("Management, Construction Management, or Entrepreneurship")
art_work_int_money = TreeNode("Architecture")

math_work_int_resp = TreeNode("Mathematics, Physics, Economics, or Accounting")
sci_work_int_resp = TreeNode("Biochemistry, Chemistry, Biology, or Physics")
lit_work_int_resp = TreeNode("English, Modern Language and Culture, Criminal Justice, or Journalism and Emerging Media")
hist_work_int_resp= TreeNode("Antrhopology")
art_work_int_resp = TreeNode("Textile and Surface Design")

math_fam_int_money = TreeNode("Data Science and Analytics")
sci_fam_int_money = TreeNode("Technical Communication")
lit_fam_int_money = TreeNode("Technical Communication")
hist_fam_int_money = TreeNode("International Affairs")
art_fam_int_money = TreeNode("Digital Animation")

math_fam_int_resp = TreeNode("Mathematics")
sci_fam_int_resp = TreeNode("Geospatial Science, or Environmental Engineering")
lit_fam_int_resp = TreeNode("English")
hist_fam_int_resp = TreeNode("Anthropology, Philosophy, or Geography")
art_fam_int_resp = TreeNode("Art, Textile and Surface Design, or Digital Animation")

math_work_ext.add_child(math_work_ext_edu)
math_work_ext.add_child(math_work_ext_noedu)
math_fam_ext.add_child(math_fam_ext_edu)
math_fam_ext.add_child(math_fam_ext_noedu)
math_work_int.add_child(math_work_int_money)
math_work_int.add_child(math_work_int_resp)
math_fam_int.add_child(math_fam_int_money)
math_fam_int.add_child(math_fam_int_money)

sci_work_ext.add_child(sci_work_ext_edu)
sci_work_ext.add_child(sci_work_ext_noedu)
sci_fam_ext.add_child(sci_fam_ext_edu)
sci_fam_ext.add_child(sci_fam_ext_noedu)
sci_work_int.add_child(sci_work_int_money)
sci_work_int.add_child(sci_work_int_resp)
sci_fam_int.add_child(sci_fam_int_money)
sci_fam_int.add_child(sci_fam_int_resp)

lit_work_ext.add_child(lit_work_ext_edu)
lit_work_ext.add_child(lit_work_ext_noedu)
lit_fam_ext.add_child(lit_fam_ext_edu)
lit_fam_ext.add_child(lit_fam_ext_noedu)
lit_work_int.add_child(lit_work_int_money)
lit_work_int.add_child(lit_work_int_resp)
lit_fam_int.add_child(lit_fam_int_money)
lit_fam_int.add_child(lit_fam_int_resp)

hist_work_ext.add_child(hist_work_ext_edu)
hist_work_ext.add_child(hist_work_ext_noedu)
hist_fam_ext.add_child(hist_fam_ext_edu)
hist_fam_ext.add_child(hist_fam_ext_noedu)
hist_work_int.add_child(hist_work_int_money)
hist_work_int.add_child(hist_work_int_resp)
hist_fam_int.add_child(hist_fam_int_money)
hist_fam_int.add_child(hist_fam_int_resp)

art_work_ext.add_child(art_work_ext_edu)
art_work_ext.add_child(art_work_ext_noedu)
art_fam_ext.add_child(art_fam_ext_edu)
art_fam_ext.add_child(art_fam_ext_noedu)
art_work_int.add_child(art_work_int_money)
art_work_int.add_child(art_work_int_resp)
art_fam_int.add_child(art_fam_int_money)
art_fam_int.add_child(art_fam_int_resp)


# Sixth Level
math_work_ext_edu_elem = TreeNode("Elementary Education")
sci_work_ext_edu_elem = TreeNode("Elementary Education")
lit_work_ext_edu_elem = TreeNode("Elementary Education or English Education")
hist_work_ext_edu_elem = TreeNode("Elementary Education or History Education")
art_work_ext_edu_elem = TreeNode("Elementary Education or Music Education")

math_work_ext_edu_mid = TreeNode("Middle Grades Education")
sci_work_ext_edu_mid = TreeNode("Middle Grades Education")
lit_work_ext_edu_mid = TreeNode("Middle Grades Education or English Education")
hist_work_ext_edu_mid = TreeNode("Middle Grades Education or History Education")
art_work_ext_edu_mid = TreeNode("Middle Grades Education or Music Education")

math_work_ext_edu_high = TreeNode("Secondary Education, Mathematics, or Physics")
sci_work_ext_edu_high = TreeNode("Secondary Education, Physics, Biology, or Chemistry")
lit_work_ext_edu_high = TreeNode("Secondary Education or English Education")
hist_work_ext_edu_high = TreeNode("Secondary Education or History Education")
art_work_ext_edu_high = TreeNode("Secondary Education or Music Education")

math_work_ext_edu_uni = TreeNode("Mathematics or Physics")
sci_work_ext_edu_uni = TreeNode("Physics, Chemistry, Biology, or Biochemistry")
lit_work_ext_edu_uni = TreeNode("English or English Education")
hist_work_ext_edu_uni = TreeNode("Geography, History or History Education")
art_work_ext_edu_uni = TreeNode("Art, Music, or Music Education")

math_fam_ext_edu_elem = TreeNode("Elementary Education")
sci_fam_ext_edu_elem = TreeNode("Elementary Education")
lit_fam_ext_edu_elem = TreeNode("Elementary Education or English Education")
hist_fam_ext_edu_elem = TreeNode("Elementary Education or History Education")
art_fam_ext_edu_elem = TreeNode("Elementary Education or Music Education")

math_fam_ext_edu_mid = TreeNode("Middle Grades Education")
sci_fam_ext_edu_mid = TreeNode("Middle Grades Education")
lit_fam_ext_edu_mid = TreeNode("Middle Grades Education or English Education")
hist_fam_ext_edu_mid = TreeNode("Middle Grades Education or History Education")
art_fam_ext_edu_mid = TreeNode("Middle Grades Education or Music Education")

math_fam_ext_edu_high = TreeNode("Secondary Education, Mathematics, or Physics")
sci_fam_ext_edu_high = TreeNode("Secondary Education, Physics, Biology, or Chemistry")
lit_fam_ext_edu_high = TreeNode("Secondary Education or English Education")
hist_fam_ext_edu_high = TreeNode("Secondary Education or History Education")
art_fam_ext_edu_high = TreeNode("Secondary Education or Music Education")

math_fam_ext_edu_uni = TreeNode("Mathematics or Physics")
sci_fam_ext_edu_uni = TreeNode("Physics, Chemistry, Biology, or Biochemistry")
lit_fam_ext_edu_uni = TreeNode("English or English Education")
hist_fam_ext_edu_uni = TreeNode("Geography, History or History Education")
art_fam_ext_edu_uni = TreeNode("Art, Music, or Music Education")

math_work_int_money_comp = TreeNode("Cybersecurity, Information Technology, Computer Science, Computer Engineering, Electrical Engineering, or Software Engineering")
math_work_int_money_nocomp = TreeNode("Mathematics, Physics")

lit_work_ext_noedu_money = TreeNode("Entrepreneurship, Management, Marketing, or Professional Sales")
lit_work_ext_noedu_resp = TreeNode("Organizational and Professional Communication, Marketing, Human Services, Criminal Justice, or Journalism and Emerging Media")
lit_fam_ext_noedu_money = TreeNode("Marketing or Psychology")
lit_fam_ext_noedu_resp = TreeNode(q5_3)

math_work_ext_edu.add_child(math_work_ext_edu_elem)
math_work_ext_edu.add_child(math_work_ext_edu_mid)
math_work_ext_edu.add_child(math_work_ext_edu_high)
math_work_ext_edu.add_child(math_work_ext_edu_uni)

math_fam_ext_edu.add_child(math_fam_ext_edu_elem)
math_fam_ext_edu.add_child(math_fam_ext_edu_mid)
math_fam_ext_edu.add_child(math_fam_ext_edu_high)
math_fam_ext_edu.add_child(math_fam_ext_edu_uni)

sci_work_ext_edu.add_child(sci_work_ext_edu_elem)
sci_work_ext_edu.add_child(sci_work_ext_edu_mid)
sci_work_ext_edu.add_child(sci_work_ext_edu_high)
sci_work_ext_edu.add_child(sci_work_ext_edu_uni)

sci_fam_ext_edu.add_child(sci_fam_ext_edu_elem)
sci_fam_ext_edu.add_child(sci_fam_ext_edu_mid)
sci_fam_ext_edu.add_child(sci_fam_ext_edu_high)
sci_fam_ext_edu.add_child(sci_fam_ext_edu_uni)

lit_work_ext_edu.add_child(lit_work_ext_edu_elem)
lit_work_ext_edu.add_child(lit_work_ext_edu_mid)
lit_work_ext_edu.add_child(lit_work_ext_edu_high)
lit_work_ext_edu.add_child(lit_work_ext_edu_uni)

lit_fam_ext_edu.add_child(lit_fam_ext_edu_elem)
lit_fam_ext_edu.add_child(lit_fam_ext_edu_mid)
lit_fam_ext_edu.add_child(lit_fam_ext_edu_high)
lit_fam_ext_edu.add_child(lit_fam_ext_edu_uni)

hist_work_ext_edu.add_child(hist_work_ext_edu_elem)
hist_work_ext_edu.add_child(hist_work_ext_edu_mid)
hist_work_ext_edu.add_child(hist_work_ext_edu_high)
hist_work_ext_edu.add_child(hist_work_ext_edu_uni)

hist_fam_ext_edu.add_child(hist_fam_ext_edu_elem)
hist_fam_ext_edu.add_child(hist_fam_ext_edu_mid)
hist_fam_ext_edu.add_child(hist_fam_ext_edu_high)
hist_fam_ext_edu.add_child(hist_fam_ext_edu_uni)

art_work_ext_edu.add_child(art_work_ext_edu_elem)
art_work_ext_edu.add_child(art_work_ext_edu_mid)
art_work_ext_edu.add_child(art_work_ext_edu_high)
art_work_ext_edu.add_child(art_work_ext_edu_uni)

art_fam_ext_edu.add_child(art_fam_ext_edu_elem)
art_fam_ext_edu.add_child(art_fam_ext_edu_mid)
art_fam_ext_edu.add_child(art_fam_ext_edu_high)
art_fam_ext_edu.add_child(art_fam_ext_edu_uni)

math_work_int_money.add_child(math_work_int_money_comp)
math_work_int_money.add_child(math_work_int_money_nocomp)

lit_work_ext_noedu.add_child(lit_work_ext_noedu_money)
lit_work_ext_noedu.add_child(lit_work_ext_noedu_resp)
lit_fam_ext_noedu.add_child(lit_fam_ext_noedu_money)
lit_fam_ext_noedu.add_child(lit_fam_ext_noedu_resp)


# Seventh Level
lit_fam_ext_noedu_resp_gen = TreeNode("Psychology, Sociology, Exercise Science, or Health and Physical Activities Leadership")
lit_fam_ext_noedu_resp_cult = TreeNode("Asian Studies, Black Studies, or Modern Language and Culture")

lit_fam_ext_noedu_resp.add_child(lit_fam_ext_noedu_resp_gen)
lit_fam_ext_noedu_resp.add_child(lit_fam_ext_noedu_resp_cult)
