cmake_minimum_required(VERSION 3.24)
project(leetcode LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

# ---------------------------------------------------------------------------
# Libreria compartida: https://gitea.com/arvazvi/c
#   - Se descarga con FetchContent.
#   - Para usar un checkout local:  -DFETCHCONTENT_SOURCE_DIR_ARVAZVI_C=/ruta/a/c
#   - Para fijar version:           -DARVAZVI_C_TAG=<commit|tag|branch>
# ---------------------------------------------------------------------------
include(FetchContent)

set(ARVAZVI_C_REPO "https://gitea.com/arvazvi/c.git" CACHE STRING "Repo de la libreria C")
set(ARVAZVI_C_TAG  "main" CACHE STRING "Tag, branch o commit de la libreria C")

FetchContent_Declare(
    arvazvi_c
    GIT_REPOSITORY ${ARVAZVI_C_REPO}
    GIT_TAG        ${ARVAZVI_C_TAG}
    GIT_SHALLOW    TRUE
)
# Solo descargamos; no usamos el Makefile del repo.
FetchContent_GetProperties(arvazvi_c)
if(NOT arvazvi_c_POPULATED)
    FetchContent_MakeAvailable(arvazvi_c)
endif()
# (arvazvi_c no tiene CMakeLists.txt, asi que MakeAvailable solo hace el clone)

file(GLOB ARVAZVI_C_SOURCES CONFIGURE_DEPENDS "${arvazvi_c_SOURCE_DIR}/src/*.c")

add_library(arvazvi_c STATIC ${ARVAZVI_C_SOURCES})
add_library(arvazvi::c ALIAS arvazvi_c)
target_include_directories(arvazvi_c PUBLIC "${arvazvi_c_SOURCE_DIR}/include")
if(NOT WIN32)
    target_link_libraries(arvazvi_c PUBLIC m)
endif()

# Unity (viene dentro de tests/unity del repo). Los tests hacen
# #include "unity/unity.h", por eso el include dir es tests/.
add_library(arvazvi_unity STATIC "${arvazvi_c_SOURCE_DIR}/tests/unity/unity.c")
add_library(arvazvi::unity ALIAS arvazvi_unity)
target_include_directories(arvazvi_unity PUBLIC "${arvazvi_c_SOURCE_DIR}/tests")
target_compile_definitions(arvazvi_unity PUBLIC UNITY_INCLUDE_DOUBLE)
target_link_libraries(arvazvi_unity PUBLIC m)

# ---------------------------------------------------------------------------
# Warnings
# ---------------------------------------------------------------------------
add_library(leetcode_warnings INTERFACE)
if(MSVC)
    target_compile_options(leetcode_warnings INTERFACE /W4)
else()
    target_compile_options(leetcode_warnings INTERFACE -Wall -Wextra)
endif()

option(LEETCODE_SANITIZE "Compilar con ASan + UBSan" OFF)
if(LEETCODE_SANITIZE AND NOT MSVC)
    target_compile_options(leetcode_warnings INTERFACE -fsanitize=address,undefined -fno-omit-frame-pointer)
    target_link_options(leetcode_warnings INTERFACE -fsanitize=address,undefined)
endif()

# ---------------------------------------------------------------------------
# Problemas: se descubre automaticamente <N>/c/
#   main.c         -> la solucion; ejecutable p<N>
#   main_test.c    -> prueba main.c; ejecutable de test p<N>_main_test.
#                     NO se enlaza con main.c: lo incluye con #include, tras
#                     renombrar su main():  #define main solution_main
#                                           #include "main.c"
#                                           #undef main
#                     (asi tambien puede probar funciones static)
#   otros *_test.c -> un test extra por archivo: p<N>_<nombre>
#   otros *.c      -> codigo auxiliar, se enlaza a main y a los tests
# ---------------------------------------------------------------------------
enable_testing()

function(leetcode_add_problem dir)
    cmake_path(GET dir PARENT_PATH problem_dir)
    cmake_path(GET problem_dir FILENAME problem)
    set(prefix "p${problem}")

    file(GLOB all_sources CONFIGURE_DEPENDS "${dir}/*.c")
    set(solution_sources "")
    set(test_sources "")
    set(main_source "")
    foreach(src IN LISTS all_sources)
        cmake_path(GET src FILENAME name)
        if(name STREQUAL "main.c")
            set(main_source "${src}")
        elseif(name MATCHES "_test\\.c$")
            list(APPEND test_sources "${src}")
        else()
            list(APPEND solution_sources "${src}")
        endif()
    endforeach()

    set(solution_lib "")
    if(solution_sources)
        set(solution_lib ${prefix}_lib)
        add_library(${solution_lib} STATIC ${solution_sources})
        target_include_directories(${solution_lib} PUBLIC "${dir}")
        target_link_libraries(${solution_lib} PUBLIC arvazvi::c PRIVATE leetcode_warnings)
    endif()

    # Si hay libreria de solucion, ya propaga arvazvi::c (evita link duplicado)
    set(base_lib ${solution_lib})
    if(NOT base_lib)
        set(base_lib arvazvi::c)
    endif()

    if(main_source)
        add_executable(${prefix} "${main_source}")
        target_link_libraries(${prefix} PRIVATE leetcode_warnings ${base_lib})
    endif()

    set(problem_targets "")
    if(main_source)
        list(APPEND problem_targets ${prefix})
    endif()

    foreach(src IN LISTS test_sources)
        cmake_path(GET src STEM name)
        set(target ${prefix}_${name})
        list(APPEND problem_targets ${target})
        add_executable(${target} "${src}")
        target_link_libraries(${target} PRIVATE arvazvi::unity leetcode_warnings ${base_lib})
        add_test(NAME ${target} COMMAND ${target})
    endforeach()

    # Target agregado: `cmake --build build --target c-<N>`
    if(problem_targets)
        add_custom_target(c-${problem} DEPENDS ${problem_targets})
    endif()
endfunction()

file(GLOB problem_c_dirs CONFIGURE_DEPENDS LIST_DIRECTORIES true "${CMAKE_CURRENT_SOURCE_DIR}/*/c")
foreach(d IN LISTS problem_c_dirs)
    if(IS_DIRECTORY "${d}")
        leetcode_add_problem("${d}")
    endif()
endforeach()
