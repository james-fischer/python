


def eval_loop():
    

    while True:
        line = input("> ")
        if line == "done":
            break
        print(eval(line))
        #print line



eval_loop()
