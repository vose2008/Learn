<h1>vim</h1>
vim 学习&使用 相关 
<h3>编码相关</h3>
vim 有四个跟字符编码方式有关的选项：  
encoding       vim 内部使用的字符编码方式，包括 buffer（缓冲区）、菜单文本、消息文本等。用户手册建议只在 .vimrc 中改变它的值，事实上似乎也只在 .vimrc 中改变才有意义  
fileencoding   vim 当前编辑的文件的字符编码方式，vim 保存文件时也会将文件保存为这种字符编码方式（不管是否新文件都是如此）  
fileencodings  vim 启动时会按照它所列出的字符编码方式逐一探测即将打开的文件的字符编码方式，并且将 fileencoding 设置为最终探测到的字符编码方式。因此最好将 Unicode 编码方式放到这个列表的最前面，将拉丁语系编码方式 latin1 放到最后面  
termencoding   vim 所工作的终端（或 windows 的 console 窗口）的字符编码方式。这个选项在windows 下对我们常用的 GUI 模式的 gVim 无效，而对 console 模式的 Vim 而言就是 windows 控制台的代码页，并且通常我们不需要改变它。  
<h5> About .vimrc.learn</h5>
跟着<a target="_blank" href="http://segmentfault.com/u/nightire">nightire</a>学Vim的配置文件（Vim的哲学 系列），受益良多  
<h5>不太熟悉的</h5>
:split 横向分屏 :vsplit 列向分屏  
Ctrl+w hjkl 移动光标 Ctrl+w HJKL 移动窗口  
Ctrl+w = + - 登高窗口 增加高度 减少高度  
C+w bt 移动到左上或者右下  
HLM 移动到屏幕顶中下部  
<h5>需要巩固的</h5>
[a,b]y 从a复制到b行  
reg 查看寄存器  
m[a-z,A-Z] 标记  
' or ` + a-z,A-Z 移动到指定标记  
<h5>神技</h5>  
寄存器复制  
"ny n 可取值  
    数字 0-9 其中0缓存最近一次复制的内容，1-9 缓存最近9次删除的内容  
    具名 a-z, A-Z 完全由用户指定内容
    选择及拖拽（selection and drop） *, +, ~，存取GUI选择文本，可用于与外部应用交互，使用前提为系统剪切板（clipboard）可用  
    -----------
v 块选择  
. 重复上一次操作  
