$(function(){function b(h){html=$.map(h,function(i){return'<span class="tags-name">'+i+'</span><sup class="tags-del"></sup> '}).join('<span class="tags-add">+</span>');$("h1").html('<span class="name">电影标签：</span>'+html)}function g(){var h=[];$(".tags-name").each(function(){h.push($(this).text())});return h}function e(){url=location.href;array=url.split("?");if(array.length==1){return""}query=array[1];arr=query.split("&");for(var h=0;h<arr.length;h++){arr2=arr[h].split("=");if(arr2[0]=="type"){if(arr2.length!=1){return arr2[1]}else{return""}}}return""}function d(i,h){$("#subject_list").html('<span class="pl">载入中，请稍候...</span>');$("#subject_list").load_withck("/j/tag/j_subject_list",{tags:i.join(" "),type:h},function(){})}function c(i,h){f(i,h)}function f(i,h){$("#related_tags").load_withck("/j/tag/j_related_tag",{tags:i.join(" "),type:h},function(){$(".more").toggle(function(){$(".tags-hide").css("display","inline");$(this).text("收起▲")},function(){$(".tags-hide").hide();$(this).text("更多▼")});$(".tags-del").click(function(){if($(this).prev().prev().text()=="+"){$(this).prev().prev().remove()}else{if($(this).next().text()=="+"){$(this).next().remove()}}$(this).prev().remove().end().remove();i=g();if(i.length===0){document.location.href="/tag/"}else{h=e();location.href="/tag/"+i.join(" ")+"?type="+h}});$(".add-tag").click(function(){i=g();i.push($(this).text());b(i);h=e();location.href="/tag/"+i.join(" ")+"?type="+h});$(".tagsInput").keypress(function(j){if(j.which==13){i=g();i.push($(this).val());b(i);h=e();location.href="/tag/"+i.join(" ")+"?type="+h}});a($(".tagsInput"))})}current=g();sort_type=e();c(current,sort_type);function a(h){if(!h.val()||h.val()==h.attr("title")){h.addClass("greyinput");h.val(h.attr("title"))}h.focus(function(){h.removeClass("greyinput");if(h.val()==h.attr("title")){h.val("")}});h.blur(function(){if(!h.val()){h.addClass("greyinput");h.val(h.attr("title"))}})}if($.browser.msie&&$.browser.version==6){$(".tags-del").hover(function(){$(this).addClass("tags-hover")},function(){$(this).removeClass("tags-hover")})}});function setHash(b){if($.browser.msie){$.locationHash(b)}else{location.hash=b}};