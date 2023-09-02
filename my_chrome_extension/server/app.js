const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors'); // Import the CORS middleware

const app = express();

// Parse JSON bodies
app.use(bodyParser.json());
// Use the CORS middleware
app.use(cors());

const PORT = process.env.PORT || 3000;

// Create MySQL connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '1234',
  database: 'bookmarks'
});

db.connect(err => {
  if (err) {
    console.error('Error connecting to MySQL database:', err);
  } else {
    console.log('Connected to MySQL database');
  }
});

// Set up routes and start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});



// ...

// Add a new video
app.post('/videos', (req, res) => {
    const { video_link } = req.body;
    console.log("Adding video ",video_link);

    const query = 'INSERT INTO videos (video_link) VALUES (?)';
    db.query(query, [video_link], (err, result) => {
      if (err) {
        console.error('Error adding video link:', err);
        res.status(500).json({ error: 'Error adding video link' });
      } else {
        res.json({ message: 'Video link added successfully' });
      }
    });
});
  
  // Get all video links
app.get('/videos', (req, res) => {
    const query = 'SELECT * FROM videos';
    db.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching video links:', err);
        res.status(500).json({ error: 'Error fetching video links' });
      } else {
        res.json(results);
      }
    });
});

app.get('/videos/:videoLink', (req, res) => {
    const videoLink = req.params.videoLink;
    console.log("Got video link: " + videoLink);
    
    const query = 'SELECT * FROM videos WHERE video_link = ?';
    db.query(query, [videoLink], (err, results) => {
      if (err) {
        console.error('Error fetching video:', err);
        res.status(500).json({ error: 'Error fetching video' });
      } else {
        if (results.length === 0) {
          res.status(404).json({ message: 'Video not found' });
        } else {
          const video = results[0];
          res.json(video);
        }
      }
    });
  });
  
  // Add a new bookmark
app.post('/bookmarks', (req, res) => {
    const { video_id, bookmark_time, description } = req.body;
    console.log("posting video bookmark ", video_id, bookmark_time, description);
    const query = 'INSERT INTO bookmarks (video_id, bookmark_time, description) VALUES (?, ?, ?)';
    db.query(query, [video_id, bookmark_time, description], (err, result) => {
      if (err) {
        console.error('Error adding bookmark:', err);
        res.status(500).json({ error: 'Error adding bookmark' });
      } else {
        res.json({ message: 'Bookmark added successfully' });
      }
    });
});
  
  // Get all bookmarks for a specific video
app.get('/bookmarks/:video_id', (req, res) => {
    const { video_id } = req.params;
    console.log("fetching bookmarks for video " + video_id);
    const query = 'SELECT * FROM bookmarks WHERE video_id = ?';
    db.query(query, [video_id], (err, results) => {
      if (err) {
        console.error('Error fetching bookmarks:', err);
        res.status(500).json({ error: 'Error fetching bookmarks' });
      } else {
        res.json(results);
      }
    });
});
  
  // ... Add routes for updating and deleting video links and bookmarks
  
  // ...
  