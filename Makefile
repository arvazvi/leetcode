.PHONY: help test-all

help:
	@echo "make go-<N>   corre los tests de <N>/go/         (ej. make go-146)"
	@echo "make py-<N>   corre los tests de <N>/py/         (ej. make py-199)"
	@echo "make test-all corre todos los tests de Go y Python"

go-%:
	@test -d $*/go || { echo "No existe $*/go/"; exit 1; }
	cd $*/go && go test ./...

py-%:
	@test -d $*/py || { echo "No existe $*/py/"; exit 1; }
	cd $*/py && python3.12 -m unittest discover -p '*_test.py' -v

test-all:
	@for d in */go/; do (cd $$d && go test ./...) || exit 1; done
	@for d in */py/; do (cd $$d && python3.12 -m unittest discover -p '*_test.py') || exit 1; done
