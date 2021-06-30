import Tree

def animal():
    # stars with a singleton
    root = Tree.Tree("bird")

    # loop until the user  quits
    while True:
        print()
        if not yes("Are you thinking of an animal?"): break

    # walk the tree
    tree = root
    while tree.left() != None:
        prompt = tree.cargo + '? '
        if yes(prompt):
            tree = tree.right
        else:
            tree = tree.left

    # make a guess
    guess = tree.cargo
    prompt = "It is a " + guess + "? "
    if yes(prompt):
        print("I rule!")
        continue

    # get new information
    prompt = "What's the animal name? "
    animal = input(prompt)
    prompt = f"What question would distinguish a {animal} from a {guess}: "
    question = input(prompt)

    # add new information to the tree
    tree.cargo