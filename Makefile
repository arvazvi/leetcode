BUILD_DIR ?= build
CMAKE_ARGS ?=

.PHONY: help configure test-all clean

help:
	@echo "make c-<N>    compila <N>/c/ y corre sus tests   (ej. make c-102)"
	@echo "make go-<N>   corre los tests de <N>/go/         (ej. make go-146)"
	@echo "make py-<N>   corre los tests de <N>/py/         (ej. make py-199)"
	@echo "make test-all corre todos los tests de C, Go y Python"
	@echo "make clean    borra $(BUILD_DIR)/"
	@echo "Opciones: CMAKE_ARGS='-DLEETCODE_SANITIZE=ON'  CMAKE_ARGS='-DARVAZVI_C_TAG=<ref>'"

# Se reconfigura siempre (barato) para detectar problemas nuevos en <N>/c/.
configure:
	@cmake -S . -B $(BUILD_DIR) $(CMAKE_ARGS) >/dev/null

c-%: configure
	@test -d $*/c || { echo "No existe $*/c/"; exit 1; }
	@cmake --build $(BUILD_DIR) --target c-$*
	@ctest --test-dir $(BUILD_DIR) -R '^p$*_' --output-on-failure --no-tests=error

go-%:
	@test -d $*/go || { echo "No existe $*/go/"; exit 1; }
	cd $*/go && go test ./...

py-%:
	@test -d $*/py || { echo "No existe $*/py/"; exit 1; }
	cd $*/py && python3.12 -m unittest discover -p '*_test.py' -v

test-all: configure
	@cmake --build $(BUILD_DIR)
	@ctest --test-dir $(BUILD_DIR) --output-on-failure
	@for d in */go/; do (cd $$d && go test ./...) || exit 1; done
	@for d in */py/; do (cd $$d && python3.12 -m unittest discover -p '*_test.py') || exit 1; done

clean:
	rm -rf $(BUILD_DIR)
