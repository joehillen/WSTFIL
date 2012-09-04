from wstfil.translate import translate

from glob import glob
import re
import traceback
import tempfile
import os
import subprocess

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
                # tf := temp file
                tf,temp = tempfile.mkstemp(suffix=".c",text=True)
                if o is not None:
                    os.write(tf, o)
                os.close(tf)

                expected = fn.rstrip('.wst')
                diff = \
                    subprocess.Popen(
                        "diff -y " + expected + " " + temp,
                        stdout=subprocess.PIPE,
                        shell=True) 
                failed = diff.wait()
                print '='*80
                if not failed:
                    print fn, "passed!"
                else:
                    for line in diff.stdout:
                        print line,
                print '='*80
                print

                os.remove(temp)
            except Exception, e:
                print "ERROR in test:",e
                print traceback.format_exc()
                
if __name__ == "__main__":
    test()
