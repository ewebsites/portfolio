window.alert("Welcome to my website! Feel free to explore!")
function myFunction() {
        var words = document.getElementById("grouppic");
        if (words.src.match("gwc22.jpg")) {
        	words.src = "gwc33.jpg";
        }
        else {
        	words.src = "gwc22.jpg";
        	}
      }
      
function myFunc() {
        var pics = document.getElementById("groupformal");
        if (pics.src.match("gwc11.jpg")) {
        	pics.src = "gwc44.jpg";
        }
        else {
        	pics.src = "gwc11.jpg";
        	}
      }
      
function bigImg(x) {
    x.style.height = "495px";
    x.style.width = "702px";
}

function normalImg(x) {
    x.style.height = "395px";
    x.style.width = "602px";
}

function moreText() {
	var text = document.getElementById("aboutmetxt");
	document.getElementById("aboutmetxt").style.fontFamily =  "Verdana, Geneva, sans-serif";
	text.innerHTML = "Outside of coding, I love volunteering and I'm very passionate about girls' rights around the world.\
		             I also love to write and I'm an editor for my school's newspaper."
}

function showHex(){
			var hex =  document.querySelector("#color_hex_value"),
			    head = document.getElementsByClassName("head");
			for(var i = 0; i < head.length; i++)
			{
   				(head.item(i)).style.color = document.querySelector("#color_picker").value;
			}
		}
