function reqeqe(){
    // location.href = "https://www.naver.com"; // get방식 요청
    // post방식 요청> form 형식으로만 가능...
    // form 없이 butten클릭하면 input내용 받아 reqParam만들어 요청
    var input_n = document.getElementById("name_input");
    var input_a = document.getElementById("age_input");
    n_ = input_n.value
    a_ = input_a.value
    
    location.href = "http://195.168.9.202/te.st?name="+n_+"&age="+a_;
    // %s 같은건 없음
    
    // document : 이 HTML 자체를 말함
}