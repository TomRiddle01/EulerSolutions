import glob   
import re
import subprocess
import hashlib
import threading
import sys
import time
import argparse
import inspect


starttime = time.time()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ok(str):
    print(bcolors.OKGREEN + str + bcolors.ENDC)
def warning(str):
    print(bcolors.WARNING + str + bcolors.ENDC)
def fail(str):
    print(bcolors.FAIL + str + bcolors.ENDC)

class EulerVerify:
    def __init__(self):
        self.files = {}
        self.scan()

    def scan(self):
        files=glob.glob("./*.py")
        match = lambda s: re.match("./([0-9]*).py", s)
        self.files = dict((int(match(file).group(1)), file) for file in files if match(file))

        with open("solutions.txt") as f:
            self.hashes = [line.strip() for line in f.readlines()]

    def executeAll(self, timeout = 10, commit_id = None):
        for i in range(max(self.files.keys())):
            if i in self.files:
                self.execute(i, timeout, commit_id)

    def execute(self, num, timeout = 10, commit_id = None):
        if num in self.files:
            if commit_id and not self.file_changed(num, commit_id):
                return

            print("Running Euler Problem #%d" % (num))
            self.solution = ""

            p = subprocess.Popen(["pypy3", str(num)+".py"], \
                stdout=subprocess.PIPE, \
                stderr=subprocess.PIPE)
            t = time.time()
            def target():
                out, err = p.communicate("")
                lines = str(out, "UTF-8").split("\n")
                if len(lines) >= 2:
                    self.solution = lines[-2]
            thread = threading.Thread(target=target)
            thread.start()

            thread.join(timeout)
            t = time.time()-t
            if thread.is_alive():
                fail("\tThread exceeded %d second time limit" % (timeout))
                p.terminate()
                thread.join()
                return
            else:
                hash = hashlib.md5(self.solution.encode('utf-8')).hexdigest()
                if self.hashes[num-1] == hash:
                    if t < 1:
                        ok("\tPassed in %.3f" % t)
                    else:
                        warning("\tPassed in %.3f" % t)
                else:
                    fail("\tWrong: Solution %s: %s != %s" % (self.solution, self.hashes[num-1], hash))

    def _verify(self, value):
        t = time.time()-starttime
        file = inspect.stack()[2][1]
        match = lambda s: re.match("([0-9]*).py", s)
        num = int(match(file).group(1))
        hash = hashlib.md5(str(value).encode("utf-8")).hexdigest()
        if self.hashes[num-1] == hash:
            if t < 1:
                ok("Passed in %.3f" % t)
            else:
                warning("Passed in %.3f" % t)
        else:
            fail("Wrong: Solution %s: " % (value))
            fail("Hashes: %s != %s" % (self.hashes[num-1], hash))
        print(value)
        exit()

    def file_changed(self, num, commit_id):
        p = subprocess.Popen(["git", "diff", commit_id, "--", str(num)+".py"], \
            stdout=subprocess.PIPE, \
            stderr=subprocess.PIPE)
        t = time.time()
        out, err = p.communicate("")

        return len(out) != 0

def verify(value):
    EulerVerify()._verify(value)




if len(sys.argv) > 1:
    timeout = 10
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('option', type=str, metavar="option", nargs=1,
                        help='number or all')
    parser.add_argument('-t', dest='timeout', default=[10], type=int, metavar="seconds",  nargs=1,
                        help='timeout for problem execution')
    parser.add_argument('-c', dest='commit_id', default=[None], type=str, metavar="commit",  nargs=1,
                        help='only execute scripts changed since this commit it')

    args = parser.parse_args()
    if "all" in args.option:
        EulerVerify().executeAll(args.timeout[0], args.commit_id[0])

    if args.option[0].isdigit():
        EulerVerify().execute(int(args.option[0]), args.commit_id[0])
