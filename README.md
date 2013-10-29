<h1>Python</h1>
<h4>Beginning Game Programming for Teens with Python</h4>
游戏问题：

<ol>
<li>兔子移动到边界还可以移动，移出到屏幕外</li>
<li>箭头发射速度-太快-虽然达不到点击即发射</li>
<li>出现箭头不能杀死獾的情况 原因不明 不报错
    <ul>
        <li>问题原因先发现大概出现在于第二到三箭后</li>
        <li>问题因该是由自己代码写问题出现的</li>
        <li>多个箭头杀死一个目标导致 .pop(index) 为空报错</li>
        <li><span style="color:red;">FIX&nbsp</span>箭头的错误出现原因为整个 # 6.3.2 块的缩进错误与上一个for循环 # 6.3 块同级了，而出现index值的错误</li>
    </ul>
</li>
<li>游戏结束后精确率的数值是float，太长了....</li>
</ol>

个人问题：(按时间顺序）

<ul>
<li>知道了.md 就是Markdown 并且兼容html 23333 我还尝试 /n </li>
<li>Git pull 什么的，哼...... 本地误删了main.py 其实用git checkout filename就好</li>
<li>vim 进阶 如查找 更大的可视区域 双档比较 替换</li>
</ul>

醍醐灌顶：

<ul>
<li>箭头与獾的碰撞不是一一记录每一只箭与每一只獾，而是当前最新的獾与箭，结果不言而喻只有两个，碰撞（死了）或者miss，这才是index与index1都要归0的原因</li>
</ul>

