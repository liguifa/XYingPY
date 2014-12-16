$(document).ready(function ()
{
    Windowload();
    $(window).scroll(function ()
    {
        var colors = new Array("bg-pink", "bg-lightBlue", "bg-orange", "bg-green", "bg-teal")
        if ($("#content").width() - $(window).scrollLeft() <= ($(window).width() + 20))
        {
            $.ajax({
                type: "get",
                url: "index.py?c=Home&a=LoadTech",
                data: {
                    pageIndex: 1
                },
                success: function (data)
                {
                    data = JSON.parse(data);
                    var w = Math.round(data.total / 2) * 390;
                    $("#content").css("width", $("#content").width() + w + "px");
                    for (var i = 0; i < data.rows.length; i++)
                    {
                        var v = parseInt(Math.random() * colors.length);
                        var str = '<div class="tile triple double-vertical ol-transparent bg-white"><div class="tile-content"><div class="panel no-border"><div class="title panel-header '+colors[v]+' fg-white">' + data.rows[i].title + '</div><div class="panel-content fg-dark nlp nrp"><img src="' + data.rows[i].url + '" class="place-left margin10 nlm ntm size2"><strong>Lorem Ipsum</strong>' + data.rows[i].body + '</div></div></div></div>';
                        $("#content").append(str);
                    }
                }
            });
        }
    });
})
function Windowload()
{
    var colors = new Array("bg-pink", "bg-lightBlue", "bg-orange", "bg-green", "bg-teal")
    listTitle = $(".title");
    for (var i = 0; i < listTitle.length; i++)
    {
        var v = Math.round(Math.random() * colors.length);
        $(listTitle[i]).addClass(colors[v]);
    }
    var w = Math.round(listTitle.length / 2) * 390;
    $("#content").css("width", w + "px");
}