export const v_null = (input) => input !== "";
export const v_min = (input, len) => input.length>=len;
export const v_max = (input, len) => input.length<=len;
export const v_txt = (input, Spcha) => {
    let idSet = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM";
    idSet += Spcha;
    for(let i =0; i<input.length;i++){
        if (idSet.indexOf(input[i])==-1){
            return false;
        }
    }
return true;};

export const v_num = (input) => input!=="" || input.indexOf(" ") == -1;

export const v_eq = (input1,input2) => input1===input2;

export const v_pw = (input,mod) => {
    let sett = "";
    if (mod == "a"){
        sett = "qwertyuiopasdfghjklzxcvbnm";}
    
    else if (mod == "A"){
        sett = "QWERTYUIOPASDFGHJKLZXCVBNM";}
    
    else if (mod == "0"){
        sett = "1234567890";}

    else {
        sett = mod;}

    for(let i = 0;i<sett.length;i++){
        if (input.indexOf(sett[i])!=-1){
            return true;
        }
    }
return false;
};

export const v_type = (input,type) => {
    type = ".("+type.replace(" ","").replace(",","|")+")$";
    type = new RegExp(type);
    return type.test(input.name);
};