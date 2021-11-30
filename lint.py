from pylint import epylint as lint
import os

files = os.listdir('./')

exceptions = ['venv', 'env', '.git', '.vscode']

for file in files:
    basename = os.path.basename(file)
    if os.path.isdir(file) and basename not in exceptions:
        lint.py_run(file)
