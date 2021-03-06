import express from 'express';
import bodyParser from 'body-parser';
import mongoose from 'mongoose';
import cors from 'cors';

import postRoutes from './routes/posts.js';
const app = express();

app.use('/posts',postRoutes);

app.use(bodyParser.urlencoded({ extended: true })).use(bodyParser.json());

app.use(cors());

const CONNECTION_URL = "mongodb+srv://yardisome:Yardisome1@cluster0.sf8tv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const PORT = process.env.PORT || 5000;

mongoose.connect(CONNECTION_URL,{useNewUrlParser : true, useUnifiedTopology: true})
.then(() => app.listen(PORT, () => console.log(`Server running on port ${PORT}`)))
.catch((error) => {console.log(error.message)});

