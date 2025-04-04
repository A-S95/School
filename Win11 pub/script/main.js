// Function for getting random number between 1 and 3 for song choose

function getRandomSongNumber() {
    return random = Math.floor(Math.random() * 3) + 1;
  }
// Function for getting random number between 1 and 3 for song choose

// Function for setting a random song
  function setNewSong() {
  if (random == 1) {
    document.getElementById("loading").src = "song/song1.mp3";
    songname.innerHTML = "Iniko - Jericho (KRSTF TECHNO Remix)";
  }
  else if (random == 2) {
    document.getElementById("loading").src = "song/song2.mp3";
    songname.innerHTML = "INTERSTELLAR live extract (vinzuel official)";
  }
  else if (random == 3) {
    document.getElementById("loading").src = "song/song3.mp3";
    songname.innerHTML = "katy perry - harleys in hawaii (s l o w e d)";
  }

  }
// Function for setting a random song

// Function for random song select on page loaded
document.addEventListener("DOMContentLoaded", function () {
    // Colocar random som 
    var random = getRandomSongNumber();
    setNewSong(random);
  });
// Function for random song select page loaded

// Function for lower or higher up sound in background, its working function in script but its not noted in text//
var play = false;
var vid = document.getElementById("loading");
vid.volume = 0.2;
window.addEventListener('keyup', function(e) {
    if (e.which == 38) { // ArrowDOWN
        vid.volume = Math.min(vid.volume + 0.025, 1);
    } else if (e.which == 40) { // ArrowUP
        vid.volume = Math.max(vid.volume - 0.025, 0);
    };
});
// Function for lower or higher up sound in background, its working function in script but its not noted in text//

var mutetext = document.getElementById("text");
var songname = document.getElementById("songname");

window.addEventListener("keyup", function(event) {
    if (event.which == 37) { // ArrowLEFT
        if (document.getElementById("loading").src.endsWith("song2.mp3")) {
            document.getElementById("loading").src = "song/song1.mp3";
            songname.innerHTML = "Iniko - Jericho (KRSTF TECHNO Remix)";

        } else if (document.getElementById("loading").src.endsWith("song1.mp3")) {
            document.getElementById("loading").src = "song/song3.mp3";
            songname.innerHTML = "katy perry - harleys in hawaii (s l o w e d)";

        } else if (document.getElementById("loading").src.endsWith("song3.mp3")) {
            document.getElementById("loading").src = "song/song2.mp3";
            songname.innerHTML = "INTERSTELLAR live extract (vinzuel official)";
        }
        document.getElementById("loading").play();
        mutetext.innerHTML = "MUTE";
    }

    if (event.which == 39) { // ArrowRIGHT
        if (document.getElementById("loading").src.endsWith("song2.mp3")) {
            document.getElementById("loading").src = "song/song3.mp3";
            songname.innerHTML = "katy perry - harleys in hawaii (s l o w e d)";

        } else if (document.getElementById("loading").src.endsWith("song3.mp3")) {
            document.getElementById("loading").src = "song/song1.mp3";
            songname.innerHTML = "Iniko - Jericho (KRSTF TECHNO Remix)";

        } else if (document.getElementById("loading").src.endsWith("song1.mp3")) {
            document.getElementById("loading").src = "song/song2.mp3";
            songname.innerHTML = "INTERSTELLAR live extract (vinzuel official)";

        }
        document.getElementById("loading").play();
        mutetext.innerHTML = "MUTE";
    }
    
});


// Function for pause and play music in background//
var audio = document.querySelector('audio');

if (audio) {

    window.addEventListener('keydown', function(event) {

        var key = event.which || event.keyCode;
        var x = document.getElementById("text").innerText;
        var y = document.getElementById("text");

        if (key === 32 && x == "MUTE") { // spacebar

            event.preventDefault();

            audio.paused ? audio.play() : audio.pause();
            y.innerHTML = "UNMUTE";

        } else if (key === 32 && x == "UNMUTE") {

            event.preventDefault();

            audio.paused ? audio.play() : audio.pause();
            y.innerHTML = "MUTE";
        }
    });
}
// Function for pause and play music in background//

//SHADED-TEXT - Function for switching words in loading animation

var shadedText = document.querySelector('.shaded-text');
var texts = ["A carregar atualizações", "A preparar o seu dispositivo", "A preparar tudo"];
var currentText = 0;

setInterval(function() {
currentText = (currentText + 1) % texts.length;
shadedText.classList.remove('fade-out');
void shadedText.offsetWidth;
shadedText.classList.add('fade-out');
setTimeout(function() {
shadedText.textContent = texts[currentText];
}, 1000);
}, 4000);
//SHADED-TEXT - Function for switching words in loading animation

//PLACEHOLDER - Function for getting handoverdata from lua script
window.addEventListener('DOMContentLoaded', () => {
  console.log(`You are connecting to ${window.nuiHandoverData.serverAddress}`);

  // a thing to note is the use of innerText, not innerHTML: names are user input and could contain bad HTML!
  document.querySelector('#namePlaceholder > span').innerText = window.nuiHandoverData.name;
});
//PLACEHOLDER - Function for getting handoverdata from lua scrip

//RANDOMPHRASES - Phrases generated after your steamname
(function welcometext() {
    var welcomes = ['Faça o que sonha com o poder da tecnologia de IA', 'Descobre os segredos.',];
    var randomWelcome = Math.floor(Math.random() * welcomes.length);
    document.getElementById('welcomeDisplay').innerHTML = welcomes[randomWelcome];
  })();