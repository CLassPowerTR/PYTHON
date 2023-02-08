import win32gui

def get_child_windows(parent):
    '''
    Ana pencerenin tüm alt pencerelerinin tutamaçlarını alın
    '''
    if not parent:
        return []

    child_windows = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), child_windows)
    return child_windows

def get_window_text(hwnd):
    '''
    Verilen tanıtıcı ile pencerenin metnini alın
    '''
    text = win32gui.GetWindowText(hwnd)
    return text

def find_child_window_by_class_name(parent, class_name):
    '''
    Verilen sınıf adına sahip ana pencerenin bir alt penceresini bulun
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
    Ana pencerede düzenleme kontrolünün tutamacını alın
    '''
    edit_control_handle = find_child_window_by_class_name(parent, 'Edit')
    return edit_control_handle

def get_render_window_handle(parent):
    '''
    Ana pencerede RenderWindow'un tanıtıcısını alın
    '''
    render_window_handle = find_child_window_by_class_name(parent, 'RenderWindow')
    return render_window_handle

def get_status_bar_handle(parent):
    '''
    Ana pencerede durum çubuğunun tutamacını alın
    '''
    status_bar_handle = find_child_window_by_class_name(parent, 'mscrls_statusbar32')
    return status_bar_handle

def getWindowHandles(hwnd):
    '''
    Verilen metnin bulunduğu pencerede Düzenleme denetiminin ve durum çubuğunun tutamaçlarını alın
    '''
    return {'Edit': get_edit_control_handle(hwnd), 'mscrls_statusbar32': get_status_bar_handle(hwnd), 'RenderWindow': get_render_window_handle(hwnd)}
    
def listWindowNames():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(getWindowHandles(hwnd),"ID=",hwnd, "TitLe= "+'"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)
