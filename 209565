var playertime=1;
var box1="null";
var box2="null";
var box3="null";
var box4="null";
var box5="null";
var box6="null";
var box7="null";
var box8="null";
var box9="null";
var p1point=0;
var p2point=0;

var schange="False";
var player1=document.getElementById("player_1");
var player2=document.getElementById("player_2");
player1.style.backgroundColor="red";
player2.style.backgroundColor="white";
if(document.getElementById("player_1").style.backgrundColor=="red"){
    playertime=1;
}

else if(player2.style.backgroundColor=="red"){
    playertime=2;
}
/* refreshwork function declearation*/
function refreshwork(winner){
     playertime=1;
    box1="null";
    box2="null";
    box3="null";
    box4="null";
    box5="null";
    box6="null";
    box7="null";
    box8="null";
    box9="null";
    schange="False";
    player1.style.backgroundColor="red";
    player2.style.backgroundColor="white";               document.getElementById("bimg_1").src="blank.jpg";
    document.getElementById("bimg_2").src="blank.jpg";
    document.getElementById("bimg_3").src="blank.jpg";
    
    document.getElementById("bimg_4").src="blank.jpg";
    document.getElementById("bimg_5").src="blank.jpg";
    document.getElementById("bimg_6").src="blank.jpg";
    
    document.getElementById("bimg_7").src="blank.jpg";
    document.getElementById("bimg_8").src="blank.jpg";
    document.getElementById("bimg_9").src="blank.jpg";
    
    if(winner==1){
        p1point+=1;
        document.getElementById("p1_ptv").innerHTML=p1point;
    }
    else if(winner==2){
        p2point+=1;
        document.getElementById("p2_ptv").innerHTML=p2point;
    }
}
/* gamework function declearation */
function gamework(element){
    if(element==document.getElementById("box_1")&&box1=="null"){
        if(playertime==1){
        
            document.getElementById("bimg_1").src="cross.png";
            box1="cross";
        }
        
       else if(playertime==2){
            document.getElementById("bimg_1").src="circle.png";
            box1="circle";
        }

       
       schange="True";
    }
    
    else if(element==document.getElementById("box_2")&&box2=="null"){
    
    if(playertime==1){
            document.getElementById("bimg_2").src="cross.png";
            box2="cross";
            
        }
        
       else if(playertime==2){
            document.getElementById("bimg_2").src="circle.png";
            box2="circle";
        }
    
    
    schange="True";
      
    }

    else if(element==document.getElementById("box_3")&&box3=="null"){
      if(playertime==1){
            document.getElementById("bimg_3").src="cross.png";
            box3="cross";
        }
        
       else if(playertime==2){
            document.getElementById("bimg_3").src="circle.png";
            box3="circle";
        }
        
        
       schange="True";
    }
    
    else if(element==document.getElementById("box_4")&&box4=="null"){
       if(playertime==1){
            document.getElementById("bimg_4").src="cross.png";
            box4="cross";
            
        }
        
       else if(playertime==2){
            document.getElementById("bimg_4").src="circle.png";
            box4="circle";
            
        }
        
       schange="True";
        
    }
    else if(element==document.getElementById("box_5")&&box5=="null"){
      if(playertime==1){
            document.getElementById("bimg_5").src="cross.png";
            box5="cross";
        }
        
       else if(playertime==2){
            document.getElementById("bimg_5").src="circle.png";
            box5="circle";
        }
      
       schange="True";
    }
    
      else if(element==document.getElementById("box_6")&&box6=="null"){
       
       if(playertime==1){
            document.getElementById("bimg_6").src="cross.png";
            box6="cross";
        }
        
       else if(playertime==2){
            document.getElementById("bimg_6").src="circle.png";
            
            box6="circle";
        }
        
        
       schange="True";
       
    }

     else if(element==document.getElementById("box_7")&&box7=="null"){
       if(playertime==1){
            document.getElementById("bimg_7").src="cross.png";
            
            box7="cross";
            
        }
        
       else if(playertime==2){
            document.getElementById("bimg_7").src="circle.png";  
              box7="circle";
                }
        
       
       schange="True";
    }
    
      else if(element==document.getElementById("box_8")&&box8=="null"){
       if(playertime==1){
            document.getElementById("bimg_8").src="cross.png";
            
            box8="cross";
            
        }
        
       else if(playertime==2){
            document.getElementById("bimg_8").src="circle.png";
            box8="circle";
        }
        
       schange="True";
        
    }
    
        else if(element==document.getElementById("box_9")&&box9=="null"){
       if(playertime==1){
            document.getElementById("bimg_9").src="cross.png";
            box9="cross";
                  }
        
       else if(playertime==2){
            document.getElementById("bimg_9").src="circle.png";
            
            box9="circle";
        }
        
        
       schange="True";
        
    }
    if(schange=="True"){
       if((box1=="cross"&&box2=="cross"&&box3=="cross")||(box1=="cross"&&box4=="cross"&&box7=="cross")||(box1=="cross"&&box5=="cross"&&box9=="cross")||(box2=="cross"&&box5=="cross"&&box8=="cross")||(box3=="cross"&&box6=="cross"&&box9=="cross")||(box3=="cross"&&box5=="cross"&&box7=="cross")||(box4=="cross"&&box5=="cross"&&box6=="cross")){
          
           var myTimeout = setTimeout(function() {
         refreshwork(1);
      }, 500);
           
       }
       
else if((box1=="circle"&&box2=="circle"&&box3=="circle")||(box1=="circle"&&box4=="circle"&&box7=="circle")||(box1=="circle"&&box5=="circle"&&box9=="circle")||(box2=="circle"&&box5=="circle"&&box8=="circle")||(box3=="circle"&&box6=="circle"&&box9=="circle")||(box3=="circle"&&box5=="circle"&&box7=="circle")||(box4=="circle"&&box5=="circle"&&box6=="circle")){
           
           var myTimeout = setTimeout(function() {
         refreshwork(2);
      }, 500);
       }
       
else if((box1=="circle"||box1=="cross")&&(box2=="circle"||box2=="cross")&&(box3=="cross"||box3=="circle")&&(box4=="circle"||box4=="cross")&&(box5=="circle"||box5=="cross")&&(box6=="circle"||box6=="cross")&&(box7=="circle"||box7=="cross")&&(box8=="cross"||box8=="circle")&&(box9=="circle"||box9=="cross")){
          
           var myTimeout = setTimeout(function() {
         refreshwork(0);
      }, 500);
       }

 
    if(player1.style.backgroundColor=="red"){
    player2.style.backgroundColor="red";
    player1.style.backgroundColor="white";
    playertime=2;
   
}

    else if(player2.style.backgroundColor=="red"){
    player2.style.backgroundColor="white";
    player1.style.backgroundColor="red";
    playertime=1;
}
schange="False";
} 
};

