import sublime, sublime_plugin

class PositionListener(sublime_plugin.EventListener):
  def on_selection_modified(self,view):
    text = "Position: "
    sels = view.sel()
    for s in sels:
        text += " " + str(s.begin())
        if not s.empty():
            text += "-" + str(s.end()) + " "
    view.set_status('exact_pos', text)