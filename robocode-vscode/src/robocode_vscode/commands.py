# Warning: Don't edit file (autogenerated from python -m dev codegen).

ROBOCODE_GET_LANGUAGE_SERVER_PYTHON = "robocode.getLanguageServerPython"  # Get a python executable suitable to start the language server.
ROBOCODE_GET_PLUGINS_DIR = "robocode.getPluginsDir"  # Get the directory for plugins.
ROBOCODE_CREATE_ACTIVITY = "robocode.createActivity"  # Create a Robocode Activity Package.
ROBOCODE_LIST_ACTIVITY_TEMPLATES_INTERNAL = "robocode.listActivityTemplates.internal"  # Provides a list with the available activity templates.
ROBOCODE_CREATE_ACTIVITY_INTERNAL = "robocode.createActivity.internal"  # Actually calls rcc to create the activity.
ROBOCODE_UPLOAD_ACTIVITY_TO_CLOUD = "robocode.uploadActivityToCloud"  # Upload activity package to the cloud.
ROBOCODE_LOCAL_LIST_ACTIVITIES_INTERNAL = "robocode.localListActivities.internal"  # Lists the activities currently available in the workspace.
ROBOCODE_IS_LOGIN_NEEDED_INTERNAL = "robocode.isLoginNeeded.internal"  # Checks if the user is already logged in.
ROBOCODE_CLOUD_LOGIN_INTERNAL = "robocode.cloudLogin.internal"  # Logs into Robocloud.
ROBOCODE_CLOUD_LIST_WORKSPACES_INTERNAL = "robocode.cloudListWorkspaces.internal"  # Lists the workspaces available for the user (in the cloud).
ROBOCODE_UPLOAD_TO_NEW_ACTIVITY_INTERNAL = "robocode.uploadToNewActivity.internal"  # Uploads an activity package as a new activity package in the cloud.
ROBOCODE_UPLOAD_TO_EXISTING_ACTIVITY_INTERNAL = "robocode.uploadToExistingActivity.internal"  # Uploads an activity package as an existing activity package in the cloud.

ALL_SERVER_COMMANDS = [
    ROBOCODE_GET_PLUGINS_DIR,
    ROBOCODE_LIST_ACTIVITY_TEMPLATES_INTERNAL,
    ROBOCODE_CREATE_ACTIVITY_INTERNAL,
    ROBOCODE_LOCAL_LIST_ACTIVITIES_INTERNAL,
    ROBOCODE_IS_LOGIN_NEEDED_INTERNAL,
    ROBOCODE_CLOUD_LOGIN_INTERNAL,
    ROBOCODE_CLOUD_LIST_WORKSPACES_INTERNAL,
    ROBOCODE_UPLOAD_TO_NEW_ACTIVITY_INTERNAL,
    ROBOCODE_UPLOAD_TO_EXISTING_ACTIVITY_INTERNAL,
]
