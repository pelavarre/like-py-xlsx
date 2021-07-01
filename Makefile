default:
	sed -i~ -n -e '1,/xlslisp.py/p' test.log
	source ~/.venvs/pips/bin/activate \
            && ./xlslisp.py --force like-py.xlsx 2>&1 |tee -a test.log
	echo '(PIPS) %' >>test.log
