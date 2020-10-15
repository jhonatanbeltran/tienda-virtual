function getID(id){
  return getElementById(id).value;
}

function innerHTML(id,result) {
  return getElementById(id).innerHTML=result;
}

function contadorCaracteres(){
  setInterval(function(){
      var c= getID("quienessomos");
      if (c.length >913) {
        innerHTML("")
      }
  },0000);
}