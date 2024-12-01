import os

# Базовый путь к папке ресурсов
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\resources"

# Папка с иконками
ICON_DIR = BASE_DIR + "\\icons"

ICON_PATH = {
    'home': os.path.join(ICON_DIR, 'home_icon.svg'),
    'projects': os.path.join(ICON_DIR, 'projects_icon.svg'),
    'tasks': os.path.join(ICON_DIR, 'tasks_icon.svg'),
    'employees': os.path.join(ICON_DIR, 'employees_icon.svg'),
    'reports': os.path.join(ICON_DIR, 'reports_icon.svg'),
    'settings': os.path.join(ICON_DIR, 'settings_icon.svg'),
    'left': os.path.join(ICON_DIR, 'left_icon.svg'),
    'right': os.path.join(ICON_DIR, 'right_icon.svg'),
    'refresh': os.path.join(ICON_DIR, 'refresh_icon.svg'),
    'search': os.path.join(ICON_DIR, 'search_icon.svg'),
}
