from wstfil.translate import translate

from glob import glob
import re
import traceback

def test():
    for fn in glob('tests/*/*.wst'):
        # Find all the test files and try to translate them
        with open(fn,'r') as f:
            m = re.match(r'.*\.(\w+)\.wst',fn)
            lang = m.group(1)
            print "Testing:", fn
            o = ""
            i = f.read()
            try:
                o = translate(lang,i)
            except Exception, e:
                print "ERROR in test:",e
                print traceback.format_exc()
            finally:
                ef = open(fn.rstrip('.wst'),'r')
                expected = ef.read()
                print '='*80
                if expected == o:
                    print fn, "passed!"
                else:
                    print fn,"failed!"
                    print o
                    print '-------------'
                    print expected
                print '='*80
                print
                
if __name__ == "__main__":
    test()
