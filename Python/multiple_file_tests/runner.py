import subprocess
import glob
from promise import Promise

def file_finder():
	count = 0
	tests = 0
	a = glob.glob("test_*.py")
	for b in a:
		f = open(b)
		contents = f.read()
		f.close()
		count = contents.count("def test_WD")
		tests = tests + count
	return tests

prc = subprocess.Popen(["pytest", "-n %i" % file_finder(), "--html=report.html"])
prc.wait()
