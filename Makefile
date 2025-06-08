CXX = g++
CXXFLAGS = -O2 -Wall -lm -static -std=gnu++20 -g
SHELL = /bin/bash

DATA_DIR := data
SRC_DIR := src
TARGET_DIR := target

all: solve

data:
	@rm -rf $(DATA_DIR)/*
	@python3 scripts/crawl_data.py --data-dir $(DATA_DIR) --problem-no $(PROBLEM_NO)

test: solve
	@python3 scripts/test.py --data-dir $(DATA_DIR) --executable $(TARGET_DIR)/solve

solve: $(TARGET_DIR)/solve

$(TARGET_DIR)/solve: $(TARGET_DIR)/solve.o
	@mkdir -p $(TARGET_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(TARGET_DIR)/solve.o: $(SRC_DIR)/solve.cpp
	@mkdir -p $(TARGET_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	@rm -rf $(TARGET_DIR)

.PHONY: data