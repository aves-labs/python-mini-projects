def strip_comments(strng, markers):
    marker_indxs = []
    white_indxs = []
    return_strng = ''
    if not markers:
        return strng
    if not strng:
        return return_strng
    for i in range(len(strng)):
        if strng[i] in markers:
            marker_indxs.append(i)
        if strng[i] == '\n':
            white_indxs.append(i)
    new_list = sorted(marker_indxs + white_indxs)
    start = 0
    for cut_point in new_list:
        if strng[cut_point] in markers:
            return_strng += strng[start:cut_point].rstrip()
            next_newline = None
            
            for nl in white_indxs:
                if nl > cut_point:
                    next_newline = nl
                    break
            if next_newline is not None:
                start = next_newline + 1
            else:
                start = len(strng)
                break
        else: 
            line_content = strng[start:cut_point].rstrip()
            return_strng += line_content + '\n'
            start = cut_point + 1
            
    if start < len(strng):
        return_strng += strng[start:].rstrip()
    
    return return_strng
