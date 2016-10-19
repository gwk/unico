# Dedicated to the public domain under CC0: https://creativecommons.org/publicdomain/zero/1.0/.

# $@: The file name of the target of the rule.
# $<: The name of the first prerequisite.
# $^: The names of all the prerequisites, with spaces between them.

.PHONY: default clean gen

default: gen

clean:
	rm unico/data_09_00.py

# all generated source targets.
gen: \
	unico/data_09_00.py


unico/data_09_00.py: gen-data.py
	./$^ data-09.0 > $@
