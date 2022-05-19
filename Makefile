#

morphic.py: src/morphic.lit
	lit --out-dir . $<

run::
	. env/bin/activate; python3 morphic.py
