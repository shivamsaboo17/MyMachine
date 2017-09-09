#!/bin/bash
set -e

echo "Testing C++ files..."
for i in $(ls -1 */*/*.cpp); do
    echo "    Compiling $i - g++ $i -lm -std=c++11"
    g++ $i -lm -std=c++11
    echo "    Running $i - ./a.out > /dev/null"
    ./a.out > /dev/null
    rm -f a.out
    echo ""
done

echo ""

echo "Testing Python files..."
for i in $(ls -1 */*/*.py); do
    echo "    Running $i - python2 $i > /dev/null"
    python2 $i > /dev/null
    echo ""
done

echo ""

echo "Running JavaScript files..."
for i in $(ls -1 */*/*.js); do
    echo "    Running $i - node --use-strict --harmony $i > /dev/null"
    node --use-strict --harmony $i > /dev/null
done