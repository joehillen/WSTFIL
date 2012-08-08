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
            o = ""
            i = f.read()
            wst = WST(lang)
            try:
                o = wst.translate(i)
            except Exception, e:
                print "ERROR:",e
            finally:
                if i == o:
                    print ".",
                else:
                    print fn,"failed!"
                    expected = open(fn.rstrip('.wst'),'r')
                    print o
                    print '==========='
                    print expected.read()
                
if __name__ == "__main__":
    test()
