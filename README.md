# pythonlogutil
python日志工具
## 安装
```
pip install pythonlog
```

## 使用
使用前需要在工程目录下新建logs目录  

### 使用默认规则
```
# -*- coding: UTF8 -*-

from pythonlog.utils.logUtil import init_logging

def testssss():
    logger = init_logging()
    logger.debug('eee')

testssss()
```

### 自定义
* 使用自定义的日志输出格式  
```
# -*- coding: UTF8 -*-

from pythonlog.utils.logUtil import init_logging

def testssss():
    logger = init_logging(path='path/*.json')
    logger.debug('eee')

testssss()
```

* 使用自定义的日志输出级别
```
# -*- coding: UTF8 -*-

from pythonlog.utils.logUtil import init_logging

def testssss():
    logger = init_logging(level='logging.INFO')
    logger.debug('eee')

testssss()
```

@author:chrishshare@163.com
