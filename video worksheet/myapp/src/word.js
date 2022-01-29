let words = 
[
    {
        value : "Hello",
        isTerm : "",
        timeStamp : "",
        search : "google.com/${this.value}",
        pause : () => {

        },
        vibrate : () => {

        },
        openOptions : () => {

        }
    }
,
    {
        value : "World",
        isTerm : "term",
        timeStamp : "00:00:00",
        search : "google.com/${this.value}",
        pause : () => {

        },
        vibrate : () => {

        },
        openOptions : () => {

        }
    }


];

function Text() {
    const text = words.map (word => <span className= {word.isTerm}>{word.value}</span>);
    return text;
}

export default Text;