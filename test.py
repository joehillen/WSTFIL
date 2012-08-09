from wstfil.translate import translate

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
            try:
                o = translate(lang,i)
            except Exception, e:
                print "ERROR:",e
            finally:
                ef = open(fn.rstrip('.wst'),'r')
                expected = ef.read()
                if expected == o:
                    print ".",
                else:
                    print fn,"failed!"
                    print o
                    print '==========='
                    print expected
                
if __name__ == "__main__":
    test()
