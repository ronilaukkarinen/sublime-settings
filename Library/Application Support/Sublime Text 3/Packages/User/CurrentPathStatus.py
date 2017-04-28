import sublime
import sublime_plugin
class CurrentPathStatusEvent(sublime_plugin.EventListener):
    def on_activated(self, view):
        view.set_status('currentPath', view.file_name())