from wstfil.wstfil import WST

# C tests
def c_helloworld():
    with open("tests/c/helloworld.c.wst") as f:
        input = f.read()
        wstc = WST("c")
        output = wstc.translate(input)
        if input == output:
            print "C Passed"
        else:
            expected = open("c/helloworld.c")
            output.split("\n")
            for n in range(len(input)):
                line = expected.readline()
                print output[n], "    |    ", line
                
if __name__ == "__main__":
    c_helloworld()
