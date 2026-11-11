function test(){ alert("테스트"); }

function for_test(){
    // for (변수 초기값; 조건식; 증감){내용}
    for (var a=1; a<5; a++){ alert(a);}
}

function while_test(){
    while (true) { var r = Math.random();
        alert(r);
        if (r>0.8){break;}
    }
}

var s = "1024연습용asdf"
s.length
s[1]
s.indexOf("용") // >> 있는경우 위치 / 없는경우 -1
s.indexOf("밥" !=-1) // >> false

// do { } while (condition);