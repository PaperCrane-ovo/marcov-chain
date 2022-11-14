def get_interval(num,type='major',root = None,cap = None):
    '''
    获取音程
    num: 音程数,比如二度,三度,八度等
    type: 音程类型,比如大三度,小三度,提供参数为major,minor
    root: 根音
    cap: 冠音
    只生成大小二三度,六度往上先咕咕...
    '''
    if root is None and cap is None:
        raise ValueError('请至少指定根音或冠音')
    type_dict = {'major':0,'minor':-1}
    if root is not None:
        cap = root + num + type_dict[type]
    elif cap is not None:
        root = cap - num - type_dict[type]
    return (root,cap)
        
def get_chord(num,type='major',root = None):
    '''
    根据指定的根音获取和弦
    num: 和弦数,比如三和弦,七和弦等
    type: 和弦类型,比如大三和弦,小三和弦等,提供参数为major,minor,diminished,augmented
    root: 根音
    '''
    if type not in ('major','minor','diminished','augmented'):
        raise ValueError('和弦类型错误,可用参数为major,minor,diminished,augmented')
    if root is None:
        raise ValueError('请指定根音')
    if num not in (3,7):
        raise ValueError('暂不支持该和弦数')
    if num == 3:
        if type == 'major':
            return (root,root+4,root+7)
        elif type == 'minor':
            return (root,root+3,root+7)
        elif type == 'diminished':
            return (root,root+3,root+6)
        elif type == 'augmented':
            return (root,root+4,root+8)
    elif num == 7:
        if type == 'major':
            return (root,root+4,root+7,root+11)
        elif type == 'minor':
            return (root,root+3,root+7,root+10)
        elif type == 'diminished':
            return (root,root+3,root+6,root+9)
        elif type == 'augmented':
            return (root,root+4,root+8,root+10)    

'''
    notes: 音级
    octaves: 音阶
    durations: 音符时值,对应4分8分16分等    
'''
notes = ('c','d','e','f','g','a','b')
relations = {'c':0,'d':1,'e':2,'f':3,'g':4,'a':5,'b':6}
octaves = ('3','4','5','6')
durations = ('4','8','16','32')