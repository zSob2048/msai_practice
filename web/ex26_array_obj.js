function array_test(){
    var a = [1,1,2,3,5,8];
    alert(a.length);
    alert(a[0]); // 범위 지정 불가 [0:2]
    
    // for (var i=0; i<a.length;i++){alert(a[i]);}
    for (var v of a){ alert(v);}
}

function obj_test(){
    // class 사용하는 정통 OOP > React때
    // class 안쓰는 obj
    var d = { name: "라이터", age: 2}; // 중괄호 < 이거로 obj
    alert(d);
    alert(d.name);
    alert(JSON.stringify(d)); // 내장 method > 객체를 문자열로 바꿔줌

}

function a_o_test(){
    var dogs = [ 
        { name: "라이터", age: 2},
        { name: "라이따", age: 1},
        { name: "랴이땨", age: 0}
    ];
    for (var d of dogs){alert(JSON.stringify(d));}
}
