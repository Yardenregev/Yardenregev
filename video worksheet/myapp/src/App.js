import './page.css';
import Earth from './earth.mp4';
import Sub from './sub.js';
function App() {
  return (
    
    <div className="App">
        <h1>Video</h1>
        <br />
        <br />
        <video src={Earth} width="720" height="500" controls autoPlay muted loop/>
        <Sub/>
    </div>
  );
}

export default App;
