from wstfil.wstfil import WST

from glob import glob
import re

def test():
    for fn in glob('tests/*/*.wst'):
        # Find all the test files and try to translate them
        with open(fn,'r') as f:
            m = re.match(r'.*\.(\w+)\.wst',fn)
            lang = m.group(1)
            print "Testing:", lang
            output = ""
            try:
                input = f.read()
                wst = WST(lang)
                output = wst.translate(input)
            except Exception, e:
                print "ERROR:",e
            finally:
                if input == output:
                    print ".",
                else:
                    print fn,"failed!"
                    expected = open(fn.rstrip('.wst'),'r')
                    output.split("\n")
                    for n in range(len(output)):
                        line = expected.readline()
                        print output[n], "    |    ", line
                
if __name__ == "__main__":
    test()
