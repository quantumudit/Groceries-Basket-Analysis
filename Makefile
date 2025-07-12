# Makefile for Groceries Basket Analysis Project
# Simple commands to make development easier

# Variables
PYTHON = python
UV = uv
PROJECT_NAME = groceries-basket-analysis

# Default target (runs when you just type 'make')
.DEFAULT_GOAL := help

# Colors for output
BLUE = \033[0;34m
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

## help: Show this help message
help:
	@echo "$(BLUE)$(PROJECT_NAME) - Available Commands:$(NC)"
	@echo ""
	@echo "  $(GREEN)install        $(NC) Install dependencies using uv"
	@echo "  $(GREEN)test           $(NC) Run all tests"
	@echo "  $(GREEN)test-cov       $(NC) Run tests with coverage report"
	@echo "  $(GREEN)lint           $(NC) Run ruff linter"
	@echo "  $(GREEN)format         $(NC) Format code with ruff"
	@echo "  $(GREEN)run            $(NC) Run the main application"
	@echo "  $(GREEN)notebook       $(NC) Start Jupyter notebook server"
	@echo "  $(GREEN)clean          $(NC) Remove cache files and build artifacts"
	@echo "  $(GREEN)pre-commit-install$(NC) Install pre-commit hooks"
	@echo "  $(GREEN)pre-commit-run $(NC) Run pre-commit on all files"
	@echo "  $(GREEN)setup          $(NC) Complete project setup (install deps + pre-commit)"
	@echo ""

## install: Install dependencies using uv
install:
	@echo "$(YELLOW)Installing dependencies...$(NC)"
	$(UV) sync --dev

## test: Run all tests
test:
	@echo "$(YELLOW)Running tests...$(NC)"
	$(UV) run pytest tests/ -v

## test-cov: Run tests with coverage report
test-cov:
	@echo "$(YELLOW)Running tests with coverage...$(NC)"
	$(UV) run pytest tests/ -v --cov=src --cov-report=term-missing

## lint: Run ruff linter
lint:
	@echo "$(YELLOW)Running linter...$(NC)"
	$(UV) run ruff check src/ tests/

## format: Format code with ruff
format:
	@echo "$(YELLOW)Formatting code...$(NC)"
	$(UV) run ruff format src/ tests/
	$(UV) run ruff check src/ tests/ --fix

## run: Run the main application
run:
	@echo "$(YELLOW)Running main application...$(NC)"
	$(UV) run python main.py

## notebook: Start Jupyter notebook server
notebook:
	@echo "$(YELLOW)Starting Jupyter notebook...$(NC)"
	$(UV) run jupyter notebook notebooks/

## clean: Remove cache files and build artifacts
clean:
	@echo "$(YELLOW)Cleaning cache files...$(NC)"
	@if exist __pycache__ rmdir /s /q __pycache__
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@if exist .ruff_cache rmdir /s /q .ruff_cache
	@if exist htmlcov rmdir /s /q htmlcov
	@if exist .coverage del /q .coverage
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /r . %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@echo "$(GREEN)Cache cleaned!$(NC)"

## pre-commit-install: Install pre-commit hooks
pre-commit-install:
	@echo "$(YELLOW)Installing pre-commit hooks...$(NC)"
	$(UV) run pre-commit install
	@echo "$(GREEN)Pre-commit hooks installed!$(NC)"

## pre-commit-run: Run pre-commit on all files
pre-commit-run:
	@echo "$(YELLOW)Running pre-commit on all files...$(NC)"
	$(UV) run pre-commit run --all-files

## setup: Complete project setup (install deps + pre-commit)
setup: install pre-commit-install
	@echo "$(GREEN)Project setup complete!$(NC)"
	@echo "$(BLUE)Next steps:$(NC)"
	@echo "  - Run 'make test' to verify everything works"
	@echo "  - Run 'make run' to execute the main application"
	@echo "  - Pre-commit hooks will run automatically on commits"

.PHONY: help install test test-cov lint format run notebook clean pre-commit-install pre-commit-run setup
