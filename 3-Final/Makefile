# INCLUDES
# --------

include .env

# GLOBALS
# -------

# Define ANSI color escape codes
ERROR = \033[0;31m
SUCCESS = \033[0;32m
INFO = \033[0;34m
NC = \033[0m 

# Define Docker and Django variables
DOCKER_COMPOSE = docker compose
DOCKER = docker
PYTHON_PATH = python3
STATICFILES_DIR = staticfiles/
DB_FILE = db.sqlite3

# DJANGO TASKS
# ------------

django-clean:
	@echo "$(INFO)[INFO] Cleaning up Django application..."
	@echo "----------------------------------------$(NC)"
	rm -rf $(STATICFILES_DIR) $(DB_FILE)
	@echo "$(SUCCESS)[SUCCESS] Django cleanup completed!\n$(NC)"

django-run:
	@echo "$(INFO)[INFO] Running Django application..."
	@echo "------------------------------------$(NC)"
	$(PYTHON_PATH) -B manage.py makemigrations
	$(PYTHON_PATH) -B manage.py migrate
	$(PYTHON_PATH) -B manage.py collectstatic --noinput
	$(PYTHON_PATH) -B manage.py createadmin
	$(PYTHON_PATH) -B manage.py accountpopulate
	$(PYTHON_PATH) -B manage.py chatpopulate
	$(PYTHON_PATH) -B manage.py runserver

# DOCKER TASKS
# ------------

docker-run:
	@echo "$(INFO)[INFO] Starting Docker containers..."
	@echo "------------------------------------$(NC)"
	$(DOCKER_COMPOSE) up -d --build
	@echo "$(SUCCESS)[SUCCESS] Docker containers started!\n$(NC)"
	@sleep 5

docker-logs:
	@echo "$(INFO)[INFO] Displaying Docker container logs..."
	@echo "------------------------------------------$(NC)"
	$(DOCKER_COMPOSE) logs -f

docker-clean:
	@echo "$(INFO)[INFO] Stopping and cleaning Docker resources.."
	@echo "-----------------------------------------------$(NC)"
	$(DOCKER_COMPOSE) down --rmi all -v --remove-orphans
	@if [ "$$( $(DOCKER) ps -aq )" ]; then \
		$(DOCKER) rm $$( $(DOCKER) ps -aq ) || true; \
	fi
	$(DOCKER) volume prune -f
	$(DOCKER) network prune -f
	$(DOCKER) image prune -f
	$(DOCKER) image prune -a -f
	$(DOCKER) builder prune -f
	@echo "$(SUCCESS)[SUCCESS] Docker cleanup completed!\n$(NC)"

docker-connect:
	@echo "$(INFO)[INFO]Connecting to PostgreSQL database..."
	@echo "------------------------------------------$(NC)"
	@$(DOCKER) exec -it $(DATABASE_CONTAINER) psql -U $(DATABASE_USER) -d $(DATABASE_DB)

# GENERAL TASKS
# -------------

run: docker-run django-run

clean: django-clean

fclean: clean docker-clean

re: fclean build run

help:
	@echo "$(INFO)[INFO] Available commands:$(NC)"
	@echo "$(INFO)  make                    - Runs the 'run' command (docker-run & django-run).$(NC)"
	@echo "$(INFO)  make clean              - Cleans Django application (django-clean).$(NC)"
	@echo "$(INFO)  make fclean             - Cleans both Django and Docker resources (clean & docker-clean).$(NC)"
	@echo "$(INFO)  make re                 - Rebuilds Docker containers and restarts Django (fclean, build, & run).$(NC)"
	@echo "$(INFO)  make help               - Displays this helper message.$(NC)"
	@echo "$(INFO)  make run                - Builds Docker containers and runs Django application (docker-run & django-run).$(NC)"
	@echo "$(INFO)  make docker-run         - Starts Docker containers.$(NC)"
	@echo "$(INFO)  make docker-clean       - Cleans Docker resources (docker-clean).$(NC)"
	@echo "$(INFO)  make docker-logs        - Displays Docker container logs.$(NC)"
	@echo "$(INFO)  make docker-connect     - Connects to PostgreSQL database.$(NC)"
	@echo "$(INFO)  make django-clean       - Cleans Django static files and database.$(NC)"
	@echo "$(INFO)  make django-run         - Runs Django migrations, collects static files, and starts the server.$(NC)"
	@echo "$(INFO)  make django-logs        - Displays Django server logs.$(NC)"

.DEFAULT_GOAL := run

.DEFAULT:
	@echo "$(ERROR)[ERROR] Unknown target '$@'. Use 'make help' to see available commands.$(NC)"
	@make help

.PHONY: clean fclean re build run help docker-run docker-clean docker-logs django-clean django-run 
