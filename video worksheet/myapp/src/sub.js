import './sub.css';
import Text from './word.js';
function Sub() {
    return (
      <div className="Sub">
          <div className="text-box">
              <div className = "sub">
                      Hello 
                      <a href="http://google.com" className ="term">
                          world
                      </a>
                      <Text/>
              </div>
          </div>
      </div>
    );
  }
  
  export default Sub;