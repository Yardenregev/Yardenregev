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
        search : "http://www.google.com",
        pause : () => {

        },
        vibrate : () => {

        },
        openOptions : () => {

        }
    }


];

function Search (value) {

}

function Text() {
    const text = words.map (
        word => <span key={word.value} className= {word.isTerm} onClick = {() => {
                                                                            if (word.isTerm === "term")
                                                                            {
                                                                            var script = `http://www.google.com/search?q=`;
                                                                            script += `${word.value}`;
                                                                            window.location.href = script;
                                                                            }
                                                                            }}
                                                                            >{word.value}</span>);
    return text;
}

export default Text;