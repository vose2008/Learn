$(document).ready(function(){
    //确定有多少个 img 标签
    var num;
    num = $(".slider>a").size()-1;
    //显示第一个 img
    var index = 0;
    var index2 = 0;
    $(".slider>a:eq("+index+")").show();
    $(".slider div:eq("+index+")").show();
    //点击 next
    $(".next").click(function(){
        $(".slider>a:eq("+index+")").hide();
        $(".slider div:eq("+index+")").hide();
        index2 = index + 1;
        if (index2>num){index2=0;}
        $(".slider>a:eq("+index2+")").show();
        $(".slider div:eq("+index2+")").show();
        index += 1;
        if (index>num){index=0;}
    });
    //点击 prev
    $(".prev").click(function(){  
        $(".slider>a:eq("+index+")").hide();
        $(".slider div:eq("+index+")").hide();
        index2 = index - 1;
        if (index2 == -1){index2=num;}
        $(".slider>a:eq("+index2+")").show();
        $(".slider div:eq("+index2+")").show();
        index -= 1;
        if (index == -1){index=num;}
    });
    //结束
});
