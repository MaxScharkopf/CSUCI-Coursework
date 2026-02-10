cmake_minimum_required(VERSION 3.10)
project(PROG01 C)

set(CMAKE_C_STANDARD 11)
add_compile_options(-Wall -g)

add_executable(echosrv echosrv-v2.c)
add_executable(echocli echocli.c)
