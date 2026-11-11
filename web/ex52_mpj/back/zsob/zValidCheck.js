function v_null(input){ return input.value; }
function v_min(input, len){ return input.value.length>=len; }
function v_max(input, len){ return input.value.length<=len; }
function v_txt(input, Spcha){
    var idSet = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM";
    idSet += Spcha;
    for(var i =0; i<input.value.length;i++){
        if (idSet.indexOf(input.value[i])==-1){
            return false;
        }
    }
return true;}

function v_num(input){
    return isNaN(input.value)||input.value.indexOf(" ") == -1;}

function v_eq(input1,input2){return input1.value==input2.value;}

function v_pw(input,mod){
    var sett = "";
    if (mod == "a"){
        sett = "qwertyuiopasdfghjklzxcvbnm";}
    
    else if (mod == "A"){
        sett = "QWERTYUIOPASDFGHJKLZXCVBNM";}
    
    else if (mod == "0"){
        sett = "1234567890";}

    else {
        sett = mod;}

    for(var i = 0;i<sett.length;i++){
        if (input.value.indexOf(sett[i])!=-1){
            return true;
        }
    }
return false;
}

function v_type(input,type){
    type = ".("+type.replace(" ","").replace(",","|")+")$";
    type = new RegExp(type);
    return (type).test(input.value);
}