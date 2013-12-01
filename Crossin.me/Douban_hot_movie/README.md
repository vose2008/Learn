<h1>抓取豆瓣评论最多的三千部电影</h1>
<h5>问题描述</h5>

<h5>目标</h5>
按评论人数高低排序豆瓣上的电影  
抓取前三千部  
额，加个原链接吧  
还需要总体评分吧  
<h5>观测到的</h5>
-------------------API-------------------------  
movie.douban.com/subject/[id]  
api.douban.com/v2/movie/subject/[id]  
ratings_count 评论总数 int  
average 评分（均分） float  
-------------------URL-------------------------  
http://movie.douban.com/tag/2011?start=0&type=T  
20 movies every page  
TODO get name id ratings  
name  
<h5>bug list</h5>
tag/2011  
<ol>
<li><b><i>FIX </i></b>page 560 剩下了什麽 | 少于10人评价 没有评分</li>
<li>page 660 太极 | 尚未上映 没有评论 没有评分</li>
</ol>
