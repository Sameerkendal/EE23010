const audioPlayer = document.getElementById('audio-player');
const nowPlayingLabel = document.getElementById('now-playing');
const shuffleButton = document.querySelector('button');
const resetButton = document.getElementById('reset-button');
const songQueue = [
    "01.mp3","02.mp3","03.mp3","04.mp3","05.mp3","06.mp3","07.mp3","08.mp3","09.mp3","10.mp3","11.mp3","12.mp3","13.mp3","14.mp3","15.mp3",
    "16.mp3","17.mp3","18.mp3","19.mp3","20.mp3","21.mp3","22.mp3","23.mp3","24.mp3","25.mp3","26.mp3","27.mp3","28.mp3","29.mp3","30.mp3",
    "31.mp3","32.mp3","33.mp3","34.mp3","35.mp3","36.mp3","37.mp3","38.mp3","39.mp3","40.mp3","41.mp3","42.mp3","43.mp3","44.mp3","45.mp3",
    "46.mp3","47.mp3"];

const originalQueue = [...songQueue];
let currentSongIndex = -1;
let isShuffled = false;
let playedSongs = [];

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function shuffleQueue() {
    if (!isShuffled) {
        shuffleArray(songQueue);
        isShuffled = true;
        playedSongs = [];
    } else {
        // If the queue is already shuffled, reset it to the original order
        songQueue.sort((a, b) => songQueue.indexOf(a) - songQueue.indexOf(b));
        isShuffled = false;
        playedSongs = [];
    }
}

function resetQueue() {
    songQueue.length = 0;
    songQueue.push(...originalQueue);
    isShuffled = false;
    playedSongs = [];
    playNextSong();
}

function updateNowPlayingLabel(index) {
    nowPlayingLabel.textContent = "Now Playing: " + songQueue[index];
}

function playSong(index) {
    if (index >= 0 && index < songQueue.length) {
        currentSongIndex = index;
        audioPlayer.src = "/audio/" + songQueue[currentSongIndex];
        audioPlayer.load();
        audioPlayer.play();
        updateNowPlayingLabel(currentSongIndex);
        playedSongs.push(currentSongIndex);
    }
}

audioPlayer.addEventListener('ended', () => {
    playNextSong();
});

function playNextSong() {
    let nextIndex;
    if (isShuffled) {
        do {
            nextIndex = Math.floor(Math.random() * songQueue.length);
        } while (playedSongs.includes(nextIndex) && playedSongs.length < songQueue.length);

        if (playedSongs.length === songQueue.length) {
            playedSongs = [];
        }
    } else {
        nextIndex = (currentSongIndex + 1) % songQueue.length;
    }
    playSong(nextIndex);
}

function playPreviousSong() {
    if (playedSongs.length > 1) {
        playedSongs.pop();
        const previousIndex = playedSongs[playedSongs.length - 1];
        playSong(previousIndex);
    } else {
        playSong(currentSongIndex);
    }
}

function playRandomSong() {
    const randomIndex = Math.floor(Math.random() * songQueue.length);
    playSong(randomIndex);
}
if (isFirstPlay) {
    playNextSong();
    isFirstPlay = false;
}
