
    Do(function() {
      // 不再提醒
      Douban.init_delete_reply_notify=function(b){var a=function(g){g.preventDefault();var c=$(g.target);var h=c[0].href.split("#")[1];$.get("/j/accounts/remove_notify?id="+h);var d=c.closest(".item-req");if($.contains($(".top-nav-reminder")[0],d[0])){d=d.parent();var f=d.siblings().length;d.fadeOut(function(){d.remove()});if(f===0){d.closest(".bd").find(".no-new-notis").show()}}else{d.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};
      Douban.init_discard_notify=function(b){var a=function(i){i.preventDefault();var c="/j/notification/discard";var f=$(i.target);var d=f[0].name;$.post_withck(c,{id:d},function(e){},"json");var g=f.closest(".item-req");if($.contains($(".top-nav-reminder")[0],g[0])){g=g.parent();var h=g.siblings().length;g.fadeOut(function(){g.remove()});if(h===0){g.closest(".bd").find(".no-new-notis").show()}}else{g.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};
      var notimenu = $('#top-nav-notimenu');
      notimenu.bind('moreitem:show', function() {
        $.ajax({
          url: 'http://www.douban.com/j/notification/nav_pop',
          data: { ck: get_cookie('ck'),
                  k: '4154040:cca449f77d26a5618d5a2337367363a248347198'
                },
          dataType: 'jsonp',
          success: function(e) {
            if (e.r) {
              return;
            }
            notimenu.html(e.s);
            if (e.n === 0) {
              $('#db-global-nav .top-nav-reminder .num').remove();
            } else {
              $('#db-global-nav .top-nav-reminder .num span').html(e.n);
            }
            if (window.load_event_monitor) {
              load_event_monitor($('#db-global-nav'));
            }
          }
        });
      });
    });
    
Do(function(){
  var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(c){c.preventDefault();var a=$(this);var b=a.parent();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show");return});$(document).click(function(a){if($(a.target).closest(".more-items").length||$(a.target).closest(".more-active").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});

    Do(function() {
      $.getScripts=function(){var b=Array.prototype.slice.call(arguments);if(!b.length){return}(function a(c){if(!c){return}if(typeof c=="function"){c();return}$.ajax({url:c,dataType:"script",cache:true,complete:function(){a(b.shift())}})})(b.shift())};
      $.getScripts(
        'http://img3.douban.com/f/shire/551ce7ff54f931bfb81b8af01942c8785f7eedf7/js/lib/jquery.tmpl.min.js',
        'http://img3.douban.com/f/movie/a197eee0a397e035a64abc25febc9b88c554f5c4/js/movie/search_sugg.js',
        function() {
         $("#db-nav-movie").find("input[name=search_text]").iSuggest({
             api: '/j/subject_suggest',
             tmplId: 'suggResult',
             item_act: function(item){
                 window.location = item.data("link");
             }
         });
      });
    });
  
Do(function(){
  var nav = $('#db-nav-movie');
  var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");if(inp.val()!==""){label.hide()}inp.parent().click(function(){inp.focus();label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){if($.trim(this.value)===""){label.show()}else{label.hide()}}).keydown(function(){label.hide()});inp.parents("form").submit(function(){if(!$.trim(inp.val()).length){return false}});nav.find(".lnk-more, .lnk-account").click(function(b){b.preventDefault();var d,a=$(this),c=a.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");if(!c.data("init")){d=a.offset();c.css({"margin-left":(d.left-$(window).width()/2-c.width()+a.width()+parseInt(a.css("padding-right"),10))+"px",left:"50%",top:d.top+a.height()+"px"});c.data("init",1);c.hide();$("body").click(function(g){var f=$(g.target);if(f.hasClass("lnk-more")||f.hasClass("lnk-account")||f.closest("#db-usr-setting").length||f.closest("#db-productions").length){return}c.hide()})}if(c.css("display")==="none"){$(".dropdown").hide();c.show()}else{$(".dropdown").hide()}});
});
