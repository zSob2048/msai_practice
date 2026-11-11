function seller_inputBclick(){
    $("#seller_inputB").click(function(){
        var c_name = $("#seller_nameI").val();
        var c_bday = $("#seller_bdayI").val();
        var c_addr = $("#seller_addrI").val();
        
        $.ajax({
            url : "http://195.168.9.202:2048/seller.reg",
            data: { "name": c_name, "bday": c_bday, "addr":c_addr},
            success: function(rresult){
                alert(rresult.result);
            seller_page = 1;
            $("#seller_listall").empty();
            seller_listappend(seller_page);
            }
        });

        $("#seller_nameI").val("");
        $("#seller_bdayI").val("");
        $("#seller_addrI").val("");
    });

}

function seller_updateBclick(){
    $("#seller_updateB").click(function(){
        var c_no = $("#seller_noU").val();
        var c_name = $("#seller_nameU").val();
        var c_addr = $("#seller_addrU").val();
        
        $.ajax({
            url : "http://195.168.9.202:2048/seller.upd",
            data: { "no":c_no, "name": c_name,  "addr":c_addr},
            success: function(rresult){
                alert(rresult.result);
            seller_page = 1;
            $("#seller_listall").empty();
            seller_listappend(seller_page);
            }
        });

    });

}

function seller_deleteBclick(){
    $("#seller_deleteB").click(function(){
        if (confirm("정말로 삭제하시겠습니까?")){
        $.ajax({
            url : "http://195.168.9.202:2048/seller.del",
            data: { "no": $("#seller_noU").val() },
            success: function(rresult){
                alert(rresult.result);
            }
        });
        $.mobile.changePage("#sellerP")
    }
    });

}

function product_inputBclick(){
    $("#product_inputB").click(function(){
        var p_name = $("#product_nameI").val();
        var p_pric = $("#product_pricI").val();
        var p_stoc = $("#product_stocI").val();
        var p_c_no = $("#product_c_noI").val();

        $.ajax({
            url : "http://195.168.9.202:2048/product.reg",
            data: { "name": p_name, "price": p_pric, "stock":p_stoc, "c_no":p_c_no},
            success: function(result){
                alert(JSON.stringify(result));
            }
        });

        $("#product_nameI").val("");
        $("#product_pricI").val("");
        $("#product_stocI").val("");
        $("#product_c_noI").val("");
    });
}

function product_updateBclick(){
    $("#product_updateB").click(function(){
        var p_no = $("#product_noU").val();
        var p_name = $("#product_nameU").val();
        var p_pric = $("#product_pricU").val();
        var p_stoc = $("#product_stocU").val();
        
        $.ajax({
            url : "http://195.168.9.202:2048/product.upd",
            data: { "no":p_no, "name": p_name,  "pric":p_pric,"stoc":p_stoc},
            success: function(rresult){
                alert(rresult.result);
            product_page = 1;
            $("#product_listall").empty();
            product_listappend(product_page);
            }
        });

    });

}

function product_deleteBclick(){
    $("#product_deleteB").click(function(){
        if (confirm("정말로 삭제하시겠습니까?")){
        $.ajax({
            url : "http://195.168.9.202:2048/product.del",
            data: { "no": $("#product_noU").val() },
            success: function(rresult){
                alert(rresult.result);
            }
        });
        $.mobile.changePage("#productP")
    }
    });

}


function seller_listappend(pg){
    $.ajax({
        url: "http://195.168.9.202:2048/seller.get",
        data:{ "page":pg,"searchkey": $("#seller_search").val()},
        success: function(seller_result){
            $.each(seller_result, function(i,s){
                var br1 = $("<br>");
                var br2 = $("<br>");
                var a = $("<a></a>").append(s.name, br1, s.bday, br2, s.addr).attr("href","#seller_detailP").attr("onclick","seller_detail("+s.no+")");
                var li = $("<li></li>").append(a);
                $("#seller_listall").append(li);
            });
            $("#seller_listall").listview("refresh");
        }
    });
}

function seller_detail(no){
    $.ajax({
        url: "http://195.168.9.202:2048/seller.ids", 
        data:{"no": no},
        success: function(seller_result){
            $("#seller_noU").val(seller_result.no);
            $("#seller_nameU").val(seller_result.name);
            $("#seller_bdayU").val(seller_result.bday);
            $("#seller_addrU").val(seller_result.addr);
        }
    });
}

function product_listappend(pg){
    $.ajax({
        url: "http://195.168.9.202:2048/product.get",
        data:{ "page":pg,"searchkey": $("#product_search").val()},
        success: function(product_result){
            $.each(product_result, function(i,s){
                var br1 = $("<br>");
                var br2 = $("<br>");
                var a = $("<a></a>").append(s.name, br1, s.pric, br2, s.stoc).attr("href","#product_detailP").attr("onclick","product_detail("+s.no+")");
                var li = $("<li></li>").append(a);
                $("#product_listall").append(li);
            });
            $("#product_listall").listview("refresh");
        }
    });
}

function product_detail(no){
    $.ajax({
        url: "http://195.168.9.202:2048/product.ids", 
        data:{"no": no},
        success: function(product_result){
            $("#product_noU").val(product_result.no);
            $("#product_nameU").val(product_result.name);
            $("#product_pricU").val(product_result.pric);
            $("#product_stocU").val(product_result.stoc);
            $("#product_c_noU").val(product_result.c_no);
        }
    });
}


function seller_addbyscroll(){
    var seller_page = 1;
    $(window).scroll(function(){
        var scroll_top = $(this).scrollTop();
        var scroll_height = $(this).height();
        var content_height = $("#sellerP").height();
        // $("#testA").text(scroll_top+","+scroll_height+","+content_height)
        if (($.mobile.activePage.attr("id") == "sellerP") &&
         (scroll_top+scroll_height>content_height+47)
        ){
            seller_page++;
            seller_listappend(seller_page);
        }
    });
}

function seller_search(){
    var keyupnum = -1;
    $("#seller_search").keyup(function(){
        // $("#testA").append("<h1>"+e.originalEvent.isComposing+"</h1>");
        seller_page = 1;
        keyupnum *= -1
            if (keyupnum == -1){seller_listappend(seller_page);
        $("#seller_listall").empty();
        }
    });
}

function product_addbyscroll(){
    var product_page = 1;
    $(window).scroll(function(){
        var scroll_top = $(this).scrollTop();
        var scroll_height = $(this).height();
        var content_height = $("#productP").height();
        if (($.mobile.activePage.attr("id") == "productP") &&
         (scroll_top+scroll_height>content_height+47)
        ){
            product_page++;
            product_listappend(product_page);
        }
    });
}

function product_search(){
    var keyupnum = -1;
    $("#seller_search").keyup(function(){
        product_page = 1;
        keyupnum *= -1
            if (keyupnum == -1){seller_listappend(product_page);
        $("#product_listall").empty();
        }
    });
}


/////////////////////////////////////////////
$(function(){
    seller_inputBclick();
    seller_updateBclick();
    seller_deleteBclick();
    seller_listappend(1); 
    seller_search();
    seller_addbyscroll();
    
    product_inputBclick();      
    product_updateBclick();
    product_deleteBclick();
    product_listappend(1); 
    product_search();
    product_addbyscroll();
});