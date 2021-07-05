default:
	sed -i~ -n -e '1,/xlslisp.py/p' make.log
	source ~/.venvs/pips/bin/activate \
            && ./xlslisp.py --force like-py.xlsx 2>&1 |tee -a make.log
	echo '(PIPS) %' >>make.log
