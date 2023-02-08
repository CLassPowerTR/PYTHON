import win32gui

def get_child_windows(parent):
    '''
    Get the handles of all child windows of the parent window
    '''
    if not parent:
        return []

    child_windows = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), child_windows)
    return child_windows

def get_window_text(hwnd):
    '''
    Get the text of the window with the given handle
    '''
    text = win32gui.GetWindowText(hwnd)
    return text

def find_child_window_by_class_name(parent, class_name):
    '''
    Find a child window of the parent window with the given class name
    '''
    if not parent:
        return None

    child_windows = get_child_windows(parent)
    for hwnd in child_windows:
        class_name_ = win32gui.GetClassName(hwnd)
        if class_name_.lower() == class_name.lower():
            return hwnd

    return None


def get_edit_control_handle(parent):
    '''
    Get the handle of the edit control in the parent window
    '''
    edit_control_handle = find_child_window_by_class_name(parent, 'Edit')
    return edit_control_handle

def get_status_bar_handle(parent):
    '''
    Get the handle of the status bar in the parent window
    '''
    status_bar_handle = find_child_window_by_class_name(parent, 'mscrls_statusbar32')
    return status_bar_handle

def getWindowHandles(hwnd):
    '''
    Get the handles of the Edit control and the status bar in the window with the given text
    '''
    edit_control_handle = get_edit_control_handle(hwnd)
    status_bar_handle = get_status_bar_handle(hwnd)
    return {'Edit': edit_control_handle, 'mscrls_statusbar32': status_bar_handle}
    
def listWindowNames():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(getWindowHandles(hwnd),"ID=",hwnd, "TitLe= "+'"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)