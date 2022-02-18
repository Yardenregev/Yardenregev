let words = 
[
    {
        value : "Hello",
        isTerm : "",
        timeStamp : "",
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
        pause : () => {

        },
        vibrate : () => {

        },
        openOptions : () => {

        }
    }


];


function Text() {
    const text = words.map (
        word => <span key={word.value} className= {word.isTerm} onClick = {() => {
                                                                            if (word.isTerm === "term")
                                                                            {
                                                                            var search = `http://www.google.com/search?q=`;
                                                                            search += `${word.value}`;
                                                                            window.location.href = search;
                                                                            }
                                                                            }}
                                                                            >
                                                                            {word.value}</span>);
    return text;
}

export default Text;