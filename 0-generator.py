from subprocess import run
import sys
from time import localtime, strftime

date = strftime("%b %-d, %Y", localtime())  # Jan 1, 2018

num, name = sys.argv[1], sys.argv[2]    # python 0-generator.py 1.4.2 barn1
fn = num + '-' + name + '.py'           # --> produce 1.4.2-barn1.py



with open(fn, 'w') as fout:
    s = '"""\nID: joshjq91\nLANG: PYTHON3\nTASK: ' + name + '\n\n'
    s += date + '\n'
    s += '"""\n\n'

    fout.write(s)

    s = "with open('" + name + ".in', 'r') as fin:\n"
    s += "    = fin.readline()\n\n\n"

    fout.write(s)

    s = "with open('" + name + ".out', 'w') as fout:\n"
    s += "    fout.write(str(result) + '\\n')\n"

    fout.write(s)

run(["gvim", "-o", fn, name + '.in', '+10', '-c', '"resize 50"'])
# when new file, in insert mode (.vimrc: autocmd BufNewFile * startinsert)
# -o: open two files in split mode
# +10: start from line 10 ('=fin.readline())

sys.exit()  # prevent terminal from lingering
